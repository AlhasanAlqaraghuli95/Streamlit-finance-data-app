import yfinance as yf
import streamlit as st

# checkbox to display data for each stock

stock = ["GOOGL", "TSLA", "MSFT"]

tickerSymbol = st.selectbox(
    label="Select stock", options = stock
)

st.header("A Simple Stock Price App")

st.subheader("We are showing the stock closing price and volume of trades for " + tickerSymbol)


# tickerSymbol = "TSLA"

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1mo', start = '2015-06-01', end = '2024-06-01')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
