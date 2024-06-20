import yfinance as yf

def stocks(nama):
    get = yf.Ticker(nama)
    print(get.history(period='6mo'))

print(stocks('META'))
