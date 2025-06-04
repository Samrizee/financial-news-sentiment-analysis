import matplotlib.pyplot as plt
def visualize(data):
    plt.figure(figsize=(14, 7))
    plt.plot(data['Date'], data['Close'], label='Close Price', color='blue')
    plt.plot(data['Date'], data['SMA_20'], label='20-Day SMA', color='orange')
    plt.title('Stock Price and Technical Indicators')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()