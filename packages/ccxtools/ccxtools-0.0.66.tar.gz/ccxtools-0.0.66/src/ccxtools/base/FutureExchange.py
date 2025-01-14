from ccxtools.base.Exchange import Exchange


class FutureExchange(Exchange):

    def __init__(self, market):
        self.market = market
        self.contract_sizes = None

    def get_contract_sizes(self):
        raise NotImplementedError

    def get_balance(self, ticker):
        raise NotImplementedError

    def get_position(self, ticker):
        raise NotImplementedError

    def post_market_order(self, ticker, side, open_close, amount):
        raise NotImplementedError

    def get_precise_order_amount(self, ticker, ticker_amount):
        raise NotImplementedError
