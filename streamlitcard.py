


import streamlit as st, pandas as pd, numpy as np, yfinance as yf
import plotly.express as px
from datetime import datetime

# Default values
default_start_date = datetime(2019, 1, 1)
default_ticker = "VANQ.L"

st.title('Stock Dashboard')
ticker = st.sidebar.text_input('Ticker',default_ticker)
start_date = st.sidebar.date_input('Start Date',default_start_date)
end_date = st.sidebar.date_input('End Date')

data = yf.download(ticker,start=start_date,end=end_date)
fig = px.line(data,x = data.index, y = data['Adj Close'],title = ticker)
st.plotly_chart(fig)

# to run streamlit
# python -m streamlit run streamlitcard.py
