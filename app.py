from flask import Flask
import ghhops_server as hs
import yfinance as yf

# register hops app as middleware
app = Flask(__name__)
hops = hs.Hops(app)


@hops.component(
    "/stockPrice",
    name="stockPrice",
    description="Gets the stock price",
    inputs=[
        hs.HopsString("T", "T", "Name of Stock"),
    ],
    outputs=[
        hs.HopsString("P", "P", "Price")
    ]
)
def stockPrice(t):
    print("was here")
    #define the ticker symbol
    tickerSymbol = t

    #get data on this ticker
    tickerData = yf.Ticker(tickerSymbol)

    #get the historical prices for this ticker
    tickerDf = tickerData.history(period='1d', start='2020-1-1', end='2025-9-27')

    #see your data
    print(tickerDf.columns)
    print(tickerDf['Close'].tolist())
    #return  = tickerDf['one'].tolist()
    return tickerDf['Close'].tolist()

if __name__ == "__main__":
    app.run()