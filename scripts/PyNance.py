import yfinance as yf

def Financial_Met(data):
    ticker = yf.Ticker(data)
    financials = ticker.financials
    return financials

