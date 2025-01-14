from decimal import Decimal
import ccxt
import time

from ccxtools.base.CcxtFutureExchange import CcxtFutureExchange


class Bybit(CcxtFutureExchange):

    def __init__(self, who, market, config):
        super().__init__(market)
        self.ccxt_inst = ccxt.bybit({
            'apiKey': config(f'BYBIT_API_KEY{who}'),
            'secret': config(f'BYBIT_SECRET_KEY{who}')
        })
        self.contract_sizes = self.get_contract_sizes()

    def get_contracts(self):
        if self.market == 'USDT':
            all_contracts = self.ccxt_inst.fetch_markets()

            filtered_contracts = []
            for contract in all_contracts:
                if not contract['active'] or not contract['linear'] or not contract['swap']:
                    continue

                filtered_contracts.append(contract)

            return filtered_contracts

    def get_contract_sizes(self):
        """
        :return: {
            'BTC': 0.1,
            'ETH': 0.01,
            ...
        }
        """
        if self.market == 'USDT':
            contracts = self.get_contracts()

            sizes = {}
            for contract in contracts:
                ticker = contract['base']
                size = float(contract['info']['lotSizeFilter']['qtyStep'])

                sizes[ticker] = size

            return sizes

    def get_position(self, ticker: str) -> float:
        # long, short 양쪽 모두 position을 갖고 있는 경우가 있음
        position = self.ccxt_inst.private_get_v5_position_list({
            'category': 'linear',
            'symbol': f'{ticker}USDT'
        })['result']['list'][0]

        absolute_size = float(position['size'])
        return absolute_size if position['side'] == 'Buy' else -absolute_size

    def post_market_order(self, ticker, side, open_close, amount):
        """
        :param ticker: <String>
        :param side: <Enum: "buy" | "sell">
        :param open_close: <Enum: "open" | "close">
        :param amount: <Float | Int>
        :return: <Float> average filled price
        """
        if self.market == 'USDT':
            symbol = f'{ticker}/USDT:USDT'

            order_id = self.ccxt_inst.create_market_order(symbol, side, amount)['id']

            for i in range(10):
                try:
                    trade_info = self.ccxt_inst.fetch_order(order_id, symbol)
                    return trade_info['average']
                except:
                    time.sleep(0.2)

    def get_max_trading_qtys(self):
        """
        :return: {
            'BTC': Decimal('100'),
            'ETH': Decimal('1000'),
            ...
        }
        """
        contracts = self.get_contracts()

        result = {}
        for contract in contracts:
            ticker = contract['base']
            result[ticker] = Decimal(contract['info']['lotSizeFilter']['maxOrderQty'])

        return result

    def get_risk_limit(self, ticker):
        """
        :param ticker: <String> ticker name ex) 'BTC', 'USDT'
        :return: [
            {
                'created_at': '2022-06-23 15:04:07.187882',
                'id': '1',
                'is_lowest_risk': '1',
                'limit': '2000000',
                'maintain_margin': '0.005',
                'max_leverage': '100',
                'section': ['1', '3', '5', '10', '25', '50', '80'],
                'starting_margin': '0.01',
                'symbol': 'BTCUSDT',
                'updated_at': '2022-06-23 15:04:07.187884'
            },
            {
                'created_at': '2022-06-23 15:04:07.187884',
                'id': '2',
                'is_lowest_risk': '0',
                'limit': '4000000',
                'maintain_margin': '0.01',
                'max_leverage': '57.15',
                'section': ['1', '2', '3', '5', '10', '25', '50'],
                'starting_margin': '0.0175',
                'symbol': 'BTCUSDT',
                'updated_at': '2022-06-23 15:04:07.187885'},
            },
            ...
        ]
        """
        if self.market == 'USDT':
            res = self.ccxt_inst.public_get_v5_market_risk_limit({
                'category': 'linear',
                'symbol': f'{ticker}USDT'
            })
            return res['result']['list']

    def set_risk_limit(self, ticker, risk_id):
        if self.market == 'USDT':
            try:
                return self.ccxt_inst.private_post_v5_position_set_risk_limit({
                    'category': 'linear',
                    'symbol': f'{ticker}USDT',
                    'risk_id': risk_id
                })
            except ccxt.errors.ExchangeError as exchange_error:
                if 'RiskId is not modified' in str(exchange_error):
                    return {
                        'ret_msg': 'OK',
                        'result': {
                            'risk_id': risk_id
                        }
                    }

                raise Exception(exchange_error)
