from interface import implements
from typing import Tuple, List, Dict, Optional
from datetime import datetime

import math
import arrow
import pandas as pd
import httpx
import json

from fast_tradier.interfaces.IBrokerAsyncClient import IBrokerAsyncClient
from fast_tradier.models.trading.OptionOrder import OptionOrder
from fast_tradier.models.trading.EquityOrder import EquityOrder
from fast_tradier.models.trading.OrderBase import OrderBase
from fast_tradier.models.account.AccountOrder import AccountOrder
from fast_tradier.models.market_data.Quote import Quote
from fast_tradier.models.account.Position import Position
from fast_tradier.models.account.AccountBalance import AccountBalance

from fast_tradier.interfaces.IRealTimeQuoteProvider import IRealTimeQuoteProvider
from fast_tradier.utils.TimeUtils import US_Eastern_TZ, YYYYMDHHMM_Format, YMD_Format, YMDHMS_Format, TimeUtils
from fast_tradier.utils.OptionUtils import OptionChain_Headers

class FastTradierAsyncClient(implements(IBrokerAsyncClient)):
    '''tradier client for interacting with Tradier API'''

    def __init__(self, access_token: str, account_id: str, is_prod: bool = True, real_time_quote_provider: Optional[IRealTimeQuoteProvider] = None, http_client: Optional[httpx.AsyncClient] = None):
        self.__bear_at = f'Bearer {access_token}'
        self.__auth_headers = {'Authorization': self.__bear_at, 'Accept': 'application/json'}
        self.__is_prod = is_prod
        self.__account_id = account_id
        self.__real_time_quote_provider = real_time_quote_provider
        self.__base_host = 'https://sandbox.tradier.com/v1/'
        self.__client = http_client
        self.__keep_client_alive = http_client is not None # keep the given client alive if not None
        if is_prod:
            self.__base_host = 'https://api.tradier.com/v1/'

    @property
    def market_open(self) -> datetime:
        return self.__market_open

    @property
    def keep_client_alive(self) -> bool:
        return self.__keep_client_alive

    @property
    def market_close(self) -> datetime:
        return self.__market_close

    @property
    def index_close(self) -> datetime:
        return self.__index_close
    
    @property
    def host_base(self) -> str:
        return self.__base_host
    
    @property
    def account_id(self) -> str:
        return self.__account_id

    def today(self) -> datetime:
        return datetime.now(US_Eastern_TZ)

    async def is_market_in_session_now_async(self) -> Tuple:
        is_open, day_arr_str, today_window = await self.is_market_open_today_async()
        if not is_open:
            return False, False

        today = self.today()
        today_str = today.strftime(YMD_Format)
        open_hour = today_window['start']
        close_hour = today_window['end']
        index_close_hour = close_hour[: -2] + '15' # index options close at 16:15

        open_t = '{} {}'.format(today_str, open_hour) # make it look like '2022-01-22 09:30'
        close_t = '{} {}'.format(today_str, close_hour)
        index_close_t = '{} {}'.format(today_str, index_close_hour)
        self.__market_open = arrow.get(open_t, YYYYMDHHMM_Format, tzinfo=US_Eastern_TZ)
        self.__market_close = arrow.get(close_t, YYYYMDHHMM_Format, tzinfo=US_Eastern_TZ)
        self.__index_close = arrow.get(index_close_t, YYYYMDHHMM_Format, tzinfo=US_Eastern_TZ)
        is_index_open = (today <= self.index_close) #whether index options trade is still open

        if today < self.market_open or today > self.market_close:
            return False, is_index_open

        return True, True
    
    async def is_market_open_today_async(self, market: str = 'NYSE') -> Tuple:
        today = self.today()
        url = 'https://api.tradier.com/v1/markets/calendar?month={}&year={}'.format(today.month, today.year)
        day_arr = []
        async with httpx.AsyncClient() as client:
            response = await client.get(url=url, headers=self.__auth_headers)
            json_res = response.json()
            day_arr = json_res["calendar"]["days"]["day"]

        today_str = today.strftime("%Y-%m-%d")
        today_open_window = None

        is_open = False
        for day in day_arr:
            if day['date'] == today_str:
                if day['status'] == 'open':
                    is_open = True
                    today_open_window = day['open']
                break

        open_day_strs = [d["date"] for d in day_arr] # e.g. ['2023-08-08']
        return is_open, open_day_strs, today_open_window
    
    # https://documentation.tradier.com/brokerage-api/markets/get-quotes
    async def get_quotes_async(self, symbols: List[str]) -> List[Quote]:
        '''get quote for symbol, could be stock or option symbol'''
        url = f'{self.host_base}markets/quotes'
        params = {'symbols': ','.join(symbols), 'greeks': 'false'}
        results = []
        async with httpx.AsyncClient() as client:
            response = await client.post(url=url, data=params, headers=self.__auth_headers)
            json_res = response.json()
            if 'quotes' in json_res and json_res['quotes'] is not None:
                quote_objs = json_res['quotes']['quote']

                if quote_objs is not None:
                    if isinstance(quote_objs, List):
                        '''API returns a list of quotes if input is a list of tickers'''
                        for quote_obj in quote_objs:
                            results.append(Quote(quote_obj))
                    elif isinstance(quote_objs, Dict):
                        '''API returns a single Dict object if input is a single ticker'''
                        results = [Quote(quote_objs)]

            return results

    async def get_order_status_async(self, order_id: int) -> Optional[str]:
        account_orders = await self.get_account_orders_async()
        for acc_order in account_orders:
            if acc_order.id == order_id:
                return acc_order.status

        return None

    async def get_account_orders_async(self) -> List[AccountOrder]:
        url = f'{self.host_base}accounts/{self.account_id}/orders'
        async with httpx.AsyncClient() as client:
            retrieved_orders = []
            response = client.get(url=url, params={'includeTags': 'true'}, headers=self.__auth_headers)
            json_res = response.json()
            if 'orders' in json_res:
                for order_json in json_res['orders']['order']:
                    retrieved_orders.append(AccountOrder(order_json))

            return retrieved_orders

    async def get_option_expirations_async(self, symbol: str) -> List[str]:
        symbol = symbol.upper()
        url = f'{self.host_base}markets/options/expirations'
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params={'symbol': symbol, 'includeAllRoots': 'true', 'strikes': 'false'}, headers=self.__auth_headers)
            json_res = response.json()
            if json_res["expirations"] is not None:
                return json_res["expirations"]["date"]

    async def place_order_async(self, order: OrderBase) -> Optional[int]:
        url = f'{self.host_base}accounts/{self.account_id}/orders'
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(url, data=order.to_json(), headers=self.__auth_headers)
                res = response.json()
                if 'order' in res and res['order']['status'].upper() == 'OK':
                    return res['order']['id']
        except Exception as ex:
            print('exception in place_option_order: ', ex)
            raise ex

    async def place_option_order_async(self, order: OptionOrder) -> Optional[int]:
        try:
            return await self.place_order_async(order)
        except Exception as ex:
            print('exception in place_option_order: ', ex)
            raise ex

    async def place_equity_order_async(self, order: EquityOrder) -> Optional[int]:
        try:
            return await self.place_order_async(order)
        except Exception as ex:
            print('exception in place_equity_order_async: ', ex)
            raise ex

    async def cancel_order_async(self, order_id: int) -> bool:
        url = f'{self.host_base}accounts/{self.account_id}/orders/{order_id}'
        try:
            async with httpx.AsyncClient() as client:
                response = await client.delete(url=url, headers=self.__auth_headers)
                res = response.json()
                if 'order' in res and 'status' in res['order']:
                    return res['order']['status'].upper() == 'OK'
        except Exception as ex:
            print('exception in cancel_order: ', ex)

        return False

    async def get_option_chain_async(self, symbol: str, expiration: str, greeks: bool = True) -> Optional[Dict]:
        url = f'{self.host_base}markets/options/chains'
        symbol = symbol.upper()

        try:
            call_options = []
            put_options = []

            async with httpx.AsyncClient() as client:
                response = await client.get(url, params={'symbol': symbol, 'expiration': expiration, 'greeks': greeks}, headers=self.__auth_headers)
                json_res = response.json()
                if json_res["options"] is not None:
                    chain = json_res["options"]["option"]
                    underlying_price = None
                    if self.__real_time_quote_provider is not None:
                        try:
                            underlying_price = self.__real_time_quote_provider.get_price(symbol)
                        except Exception as inner_ex:
                            print('exception getting real time quote: ', inner_ex)
                    else:
                        symbol_quotes = await self.get_quotes_async([symbol])
                        if len(symbol_quotes) > 0 and underlying_price is None:
                            underlying_price = symbol_quotes[0].last

                    now_unixts = int(arrow.utcnow().datetime.timestamp())
                    for o in chain:
                        gamma = 0
                        delta = 0
                        vega = 0
                        greeks_nums = o['greeks']
                        if greeks_nums is not None: 
                            gamma = greeks_nums['gamma'] if greeks_nums['gamma'] is not None and not math.isnan(greeks_nums['gamma']) else 0
                            delta = greeks_nums['delta'] if greeks_nums['delta'] is not None and not math.isnan(greeks_nums['delta']) else 0
                            vega = greeks_nums['vega'] if greeks_nums['vega'] is not None and not math.isnan(greeks_nums['vega']) else 0

                        row = o['symbol'], o['strike'], 0 if pd.isna(o['last']) else o['last'], o['open_interest'], o['ask'], o['bid'], o['expiration_date'], TimeUtils.convert_unix_ts(o['bid_date']).strftime(YMDHMS_Format), o['volume'], underlying_price, now_unixts, gamma, delta, vega
                        if o['option_type'] == 'call':
                            call_options.append(row)
                        else:
                            put_options.append(row)

                call_df = pd.DataFrame(call_options)
                call_df.columns = OptionChain_Headers
                put_df = pd.DataFrame(put_options)
                put_df.columns = OptionChain_Headers
                return {
                    'expiration': expiration,
                    'ticker': symbol,
                    'call_chain': call_df,
                    'put_chain': put_df
                    }
        except Exception as ex:
            return None

    async def modify_option_order_async(self, modified_order: OptionOrder) -> bool:
        url = f'{self.host_base}accounts/{self.account_id}/orders/{modified_order.id}'
        try:
            async with httpx.AsyncClient() as client:
                response = await client.put(url=url, data=modified_order.to_json(), headers=self.__auth_headers)
                res = response.json()
                if 'order' in res and 'status' in res['order']:
                    return res['order']['status'].upper() == 'OK'
                return False
        except Exception as ex:
            return False
    
    async def get_positions_async(self) -> List[Position]:
        url = f'{self.host_base}accounts/{self.account_id}/positions'
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(url=url,
                                            params={},
                                            headers=self.__auth_headers)
                res = response.json()
                results = []
                if 'position' in res['positions']:
                    for position_dict in res['positions']['position']:
                        results.append(Position(position_dict))
                return results
        except Exception as ex:
            return []

    async def get_account_balance_async(self) -> Optional[AccountBalance]:
        url = f'{self.host_base}accounts/{self.account_id}/balances'
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(url=url,
                                            params={},
                                            headers=self.__auth_headers)
                res = response.json()
                if 'balances' in res:
                    return AccountBalance(res['balances'])
        except Exception as ex:
            print('exception in get_account_balances: ', ex)

        return None