import csv
from collections import namedtuple
from urllib2 import urlopen
yahoo_url = ('http://download.finance.yahoo.com/d/quotes.csv?s=%s&f=sl1d1t1c1ohgv&e=.csv')
Trade = namedtuple('Trade', ['symbol', 'volume', 'price'])

def load_portfolio(path):
    with open(path) as fo:
        trades = []
        for symbol, volume, price in csv.reader(fo):
            trades.append(Trade(symbol, int(volume), float(price)))
        return trades
def get_quote(symbol):
    fp = urlopen(yahoo_url % symbol)
    reader = csv.reader(fp)
    fields = reader.next()
    return float(fields[1])


if __name__ =='__main__':
    trades = load_portfolio('stocks.csv')
