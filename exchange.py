from binance.client import Client

class exchange:

    """
    建構式

    Args:
        apiKey (str): API金鑰
        apiSecret (str): API密鑰

    Returns:
        void
    """
    def __init__(self, apiKey: str, apiSecret: str):
        self.client = Client(apiKey, apiSecret)

    """
    取得當前價格

    Args:
        symbol (str): 要取得價格的標的，例BTCUSDT

    Returns:
        float: 當前的價格
    """
    def getSymbolPrice(self, symbol: str) -> float:
        prices = self.client.get_all_tickers()
        num = len(prices)
        price = 0
        for i in range(num):
            if symbol == prices[i]['symbol']:
                price = prices[i]['price']
        return price

    """
    進行交易

    Args:
        symbol (str): 要取得價格的標的，例BTCUSDT
        side (str): 要買進用buy，要賣出用sell
        quantity (float): 要買進的數量

    Returns:
        str: API response
    """
    def doExchange(self, symbol: str, side: str, quantity: float):
        sides = {'buy': Client.SIDE_BUY, 'sell': Client.SIDE_SELL}
        order = self.client.create_test_order(
            symbol=symbol,
            side=sides[side],
            type=Client.ORDER_TYPE_MARKET,
            quantity=quantity
        )
        return order

"""
公私鑰請到以下網址申請
https://www.binance.com/userCenter/createApi.html

開發文件參考如下
https://github.com/binance-exchange/python-binance
https://python-binance.readthedocs.io/en/latest/
"""

#API公鑰
apiKey = ''

#API私鑰
apiSecret = 'NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j'

#新增交易物件
exchange = exchange(apiKey, apiSecret)

#買賣標的
symbol = 'BTCUSDT'

#取得當前價格
price = exchange.getSymbolPrice(symbol)

"""
範例

if (price >= 9200):
    order = exchange.doExchange(symbol, 'sell', 100.5)
if (price <= 6800):
    order = exchange.doExchange(symbol, 'sell', 100.5)
if (price <= 3000):
    order = exchange.doExchange(symbol, 'buy', 100.5)
"""