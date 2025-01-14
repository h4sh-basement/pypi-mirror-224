from decimal import Decimal
import math
import pytest
from src.ccxtools.tools import get_env_vars
from src.ccxtools.bybit import Bybit


@pytest.fixture
def config():
    return get_env_vars()


@pytest.fixture
def bybit(config):
    return Bybit('', 'USDT', config)


def test_get_contract_sizes(bybit):
    sizes = bybit.get_contract_sizes()
    assert isinstance(sizes, dict)
    assert sizes['BTC'] == 0.001
    assert sizes['ETH'] == 0.01


def test_get_balance(bybit):
    # Test input Start
    ticker = 'USDT'
    balance_input = 3758.20245937
    # Test input End

    balance = bybit.get_balance(ticker)
    assert balance_input * 0.9 <= balance <= balance_input * 1.1


def test_get_position(bybit):
    # Test input Start
    ticker = 'STG'
    amount = -2180
    # Test input End

    position = bybit.get_position(ticker)
    assert isinstance(position, float)
    if amount:
        assert math.isclose(position, amount)


def test_post_market_order(bybit):
    # Test input Start
    ticker = 'XRP'
    amount = 20
    # Test input End

    last_price = bybit.ccxt_inst.fetch_ticker(f'{ticker}/USDT')['last']

    buy_open_price = bybit.post_market_order(ticker, 'buy', 'open', amount)
    assert 0.9 * last_price < buy_open_price < 1.1 * last_price
    sell_close_price = bybit.post_market_order(ticker, 'sell', 'close', amount)
    assert 0.9 * last_price < sell_close_price < 1.1 * last_price
    sell_open_price = bybit.post_market_order(ticker, 'sell', 'open', amount)
    assert 0.9 * last_price < sell_open_price < 1.1 * last_price
    buy_close_price = bybit.post_market_order(ticker, 'buy', 'close', amount)
    assert 0.9 * last_price < buy_close_price < 1.1 * last_price


def test_get_precise_order_amount(bybit):
    ticker = 'BTC'
    ticker_amount = 0.0011
    assert bybit.get_precise_order_amount(ticker, ticker_amount) == 0.001


def test_get_max_trading_qtys(bybit):
    # Test input Start
    result = {
        'BTC': Decimal('100'),
        'ETH': Decimal('1500'),
        'EOS': Decimal('55000'),
        'XRP': Decimal('1800000'),
    }
    # Test input End

    max_trading_qtys = bybit.get_max_trading_qtys()
    for ticker, qty in result.items():
        assert ticker in max_trading_qtys
        assert max_trading_qtys[ticker] == qty


def test_get_risk_limit(bybit):
    # Test input start
    ticker = 'BTC'
    # Test input end

    risk_limit = bybit.get_risk_limit(ticker)
    assert risk_limit[0]['symbol'] == f'{ticker}USDT'


def test_set_risk_limit(bybit):
    # Test input start
    ticker = 'BTC'
    risk_id = 2
    # Test input end

    response = bybit.set_risk_limit(ticker, risk_id)
    assert response['ret_msg'] == 'OK'
    assert int(response['result']['risk_id']) == risk_id
