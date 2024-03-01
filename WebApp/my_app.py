import yfinance as yf
import streamlit as st
import pandas as pd

# header of web app
st.write("""
# Simple stock price app

Shown are the stock closing price & volume of google
""")

tickerSymbol = 'GOOGL'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period = "id", start="2010-5-31", end="2020-5-31")

# open high lowClose Volume DividentsStocks Sprin
# we are gn to show close price & volume in app

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)