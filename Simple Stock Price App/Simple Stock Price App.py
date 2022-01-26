import yfinance as yf
import streamlit as st

st.write("""
# Simple Stock Price App / Aplicacion simple del precio de acciones 
Shown are the stock **closing price** and ***volume*** of Bitcoin!
""")

#define the ticker symbol
tickerSymbol = 'BTC-USD'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2014-9-14', end='2022-1-20')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)
