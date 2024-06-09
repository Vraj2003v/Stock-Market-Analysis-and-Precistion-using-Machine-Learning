import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

# Adjust the display size of the main container
st.markdown(
    """
    <style>
        /* Set width and height of the main container */
        .stApp {
            width: 1020px; /* Adjust the width as needed */
            height: 2900px; /* Adjust the height as needed */
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
selected_stock = 'Infosys Ltd. (INFY)'

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
selected_time_frame_key = st.selectbox(
    "Select Time Frame", list(time_frames.keys()), index=len(time_frames) - 1
)
selected_time_frame = time_frames[selected_time_frame_key]

# Fetch real-time stock data
@st.cache_data
def get_stock_data(symbol, period):
    data = yf.download(symbol, period=period)
    return data

stock_data = get_stock_data('INFY.NS', selected_time_frame_key)

# Print the name of the selected stock at the top
st.write(" ")
st.write(f"# {selected_stock} ")
st.write(" ")

# Display latest closing and opening prices with currencies
latest_date = stock_data.index[-1].strftime('%Y-%m-%d')
latest_close_price = stock_data['Close'][-1]
latest_open_price = stock_data['Open'][-1]
latest_high_price = stock_data['High'][-1]
latest_low_price = stock_data['Low'][-1]

currency_symbol = '₹'  # Indian Rupee for Infosys

latest_open_text = f"Latest Opening Price ({latest_date}): {currency_symbol}  {latest_open_price:.2f}"
latest_close_text = f"Latest Closing Price ({latest_date}): {currency_symbol}  {latest_close_price:.2f}"
latest_high_text = f"Latest Day High Price ({latest_date}): {currency_symbol}  {latest_high_price:.2f}"
latest_low_text = f"Latest Day Low Price ({latest_date}): {currency_symbol}  {latest_low_price:.2f}"

st.write(
    f"<div style='font-size: 22px; text-align: left;'>{latest_open_text}</div>",
    unsafe_allow_html=True
)

st.write(
    f"<div style='font-size: 22px; text-align: left;'>{latest_close_text}</div>",
    unsafe_allow_html=True
)

st.write(
    f"<div style='font-size: 22px; text-align: left;'>{latest_high_text}</div>",
    unsafe_allow_html=True
)

st.write(
    f"<div style='font-size: 22px; text-align: left;'>{latest_low_text}</div>",
    unsafe_allow_html=True
)

st.write(" ")
st.write(" ")

# Plot the stock data
fig_close = go.Figure()
fig_close.add_trace(go.Scatter(x=stock_data.index, y=stock_data['Close'], mode='lines', name='Close'))
fig_close.update_layout(
    title={
        'text': f"{selected_stock} Close Price ({selected_time_frame})",
        'font': {'size': 30}  # Increase font size to 35 pixels
    },
    xaxis_title="Date",
    yaxis_title="Price",
    width=675,  # Adjust width
)

st.plotly_chart(fig_close)

fig_open = go.Figure()
fig_open.add_trace(go.Scatter(x=stock_data.index, y=stock_data['Open'], mode='lines', name='Open'))
fig_open.update_layout(
    title={
        'text': f"{selected_stock} Open Price ({selected_time_frame})",
        'font': {'size': 30}  # Increase font size to 35 pixels
    },
    xaxis_title="Date",
    yaxis_title="Price",
    width=675,  # Adjust width
)

st.plotly_chart(fig_open)

fig_high = go.Figure()
fig_high.add_trace(go.Scatter(x=stock_data.index, y=stock_data['High'], mode='lines', name='High'))
fig_high.update_layout(
    title={
        'text': f"{selected_stock} Day High Price ({selected_time_frame})",
        'font': {'size': 30}  # Increase font size to 35 pixels
    },
    xaxis_title="Date",
    yaxis_title="Price",
    width=675,  # Adjust width
)

st.plotly_chart(fig_high)

fig_low = go.Figure()
fig_low.add_trace(go.Scatter(x=stock_data.index, y=stock_data['Low'], mode='lines', name='Low'))
fig_low.update_layout(
    title={
        'text': f"{selected_stock} Day Low Price ({selected_time_frame})",
        'font': {'size': 30}  # Increase font size to 35 pixels
    },
    xaxis_title="Date",
    yaxis_title="Price",
    width=675,  # Adjust width
)

st.plotly_chart(fig_low)
