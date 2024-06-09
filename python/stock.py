import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

# Function to get currency symbol from stock symbol
def get_currency_symbol(symbol):
    if symbol.endswith('.NS'):
        return '₹'  # Indian Rupee
    else:
        return '$'  # US Dollar (default assumption)

# Adjust the display size of the main container
st.markdown(
    """
    <style>
        /* Set width and height of the main container */
        .stApp {
            width: 850px; /* Adjust the width as needed */
            height: 820px; /* Adjust the height as needed */
            overflow: hidden; /* Hide overflow */
        }

        /* Hide vertical scrollbar for the whole page */
        body {
            overflow: hidden;
            margin: 0; /* Reset margin */
            padding-bottom: 0px; /* Reduce bottom padding */
            padding : 0px; 
        }

        header {
            visibility: hidden;
        }

        /* Remove excess space */
        div[data-testid='stBlock'] div[data-testid='stBlockSpacer'] {
            margin-top: 0;
            margin-bottom: 0; /* Remove bottom margin */
        }
    </style>
""",
    unsafe_allow_html=True,
)

# Sidebar for user input
stocks = {
    'Apple Inc.': 'AAPL',
    'Google': 'GOOGL',
    'Microsoft Corporation': 'MSFT',
    'Tesla Inc.': 'TSLA',
    'Amazon': 'AMZN',
    'Reliance Industries Limited': 'RELIANCE.NS',
    'TCS': 'TCS.NS',
    'Infosys': 'INFY.NS',
    'State Bank of India': 'SBIN.NS',
    'HDFC Bank': 'HDFCBANK.NS',
    # Add more stocks as needed
}

selected_stock = st.sidebar.selectbox("Select Stock", list(stocks.keys()))

time_frames = {
    '2d': '2 Day',
    '5d': '5 Days',
    '1mo': '1 Month',
    '3mo': '3 Months',
    '6mo': '6 Months',
    '1y': '1 Year',
    '5y': '5 Years',
    '10y': '10 Years',
    'max': 'All'
}
selected_time_frame_key = st.sidebar.selectbox(
    "Select Time Frame", list(time_frames.keys()), index=len(time_frames) - 1
)
selected_time_frame = time_frames[selected_time_frame_key]

# Fetch real-time stock data
@st.cache_data
def get_stock_data(symbol, period):
    data = yf.download(symbol, period=period)
    return data

stock_data = get_stock_data(stocks[selected_stock], selected_time_frame_key)

# Plot the stock data
fig = go.Figure()
fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['Close'], mode='lines', name='Close'))
fig.update_layout(
    title={
        'text': f"{selected_stock} Stock Price ({selected_time_frame})",
        'font': {'size': 35}  # Increase font size to 35 pixels
    },
    xaxis_title="Date",
    yaxis_title="Price",
    width=750,  # Adjust width
)

st.plotly_chart(fig)

# Display latest closing and opening prices with currencies
latest_date = stock_data.index[-1].strftime('%Y-%m-%d')
latest_close_price = stock_data['Close'][-1]
latest_open_price = stock_data['Open'][-1]

currency_symbol = get_currency_symbol(stocks[selected_stock])

latest_open_text = f"Latest Opening Price ({latest_date}): {currency_symbol}  {latest_open_price:.2f}"
latest_close_text = f"Latest Closing Price ({latest_date}): {currency_symbol}  {latest_close_price:.2f}"

st.write(
    f"<div style='font-size: 22px; text-align: center;'>{latest_open_text}</div>",
    unsafe_allow_html=True
)

st.write(
    f"<div style='font-size: 22px; text-align: center;'>{latest_close_text}</div>",
    unsafe_allow_html=True
)
