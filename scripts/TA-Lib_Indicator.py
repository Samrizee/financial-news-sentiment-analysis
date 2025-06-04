import talib

def Technical_Analyser(data):
    data['SMA_20'] = talib.SMA(data['Close'], timeperiod=20)
    data['RSI'] = talib.RSI(data['Close'], timeperiod=14)
    data['MACD'], data['MACD_signal'], _ = talib.MACD(data['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
    print(data[['Close', 'SMA_20', 'RSI', 'MACD', 'MACD_signal']].head())