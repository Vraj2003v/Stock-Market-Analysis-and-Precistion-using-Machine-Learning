import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
from yahoo_fin.stock_info import get_data
from streamlit_option_menu import option_menu
import warnings
warnings.filterwarnings('ignore')
import sklearn.metrics as metrics

# Set the layout as wide
st.set_page_config(layout="wide")

# Adjust the display size of the main container
st.markdown(
    """
    <style>
        /* Set width and height of the main container */
        .stApp {
            width: 1020px; /* Adjust the width as needed */
            height: 900px; /* Adjust the height as needed */
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

        /* Adjust selectbox size and center align */
        div[data-testid="stSelectbox"] > div:first-child {
            width: 50%; /* Adjust the width as needed */
            margin: 0 auto; /* Center align */
        }
    </style>
""",
    unsafe_allow_html=True,
)

def get_stock_data(ticker):
    df = get_data(ticker, start_date=None, end_date=None, index_as_date=False, interval='1d')
    return df

def get_currency_symbol(ticker):
    # Dictionary mapping ticker symbols to currency symbols
    currency_symbols = {
        'AAPL': '$',
        'GOOGL': '$',
        'MSFT': '$',
        'TSLA': '$',
        'AMZN': '$',
        'RELIANCE.NS': '₹',
        'TCS.NS': '₹',
        'INFY.NS': '₹',
        'SBIN.NS': '₹',
        'HDFCBANK.NS': '₹'
    }
    return currency_symbols.get(ticker, '')

def main():
    st.title("Latest Closing Price Predictor")
    ticker = st.selectbox("Pick any stock or index to predict:",
                          ('AAPL', 'GOOGL', 'MSFT', 'TSLA', 'AMZN', 'RELIANCE.NS', 'TCS.NS', 'INFY.NS', 'SBIN.NS', 'HDFCBANK.NS'))

    if st.button('Predict'):
        with st.spinner('Predicting...'):
            df = get_stock_data(ticker)
            ## ------------------------------- PREDICTION LOGIC -------------------------------
            # Data Cleaning
            mean = df['open'].mean()
            df['open'] = df['open'].fillna(mean)

            mean = df['high'].mean()
            df['high'] = df['high'].fillna(mean)

            mean = df['low'].mean()
            df['low'] = df['low'].fillna(mean)

            mean = df['close'].mean()
            df['close'] = df['close'].fillna(mean)

            X = df[['open', 'high', 'low']]
            y = df['close'].values.reshape(-1, 1)

            # Splitting our dataset to Training and Testing dataset
            from sklearn.model_selection import train_test_split
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            # Fitting Linear Regression to the training set
            from sklearn.linear_model import LinearRegression
            reg = LinearRegression()
            reg.fit(X_train, y_train)

            # Predicting the Test set result
            y_pred = reg.predict(X_test)
            o = df['open'].values
            h = df['high'].values
            l = df['low'].values

            n = len(df)

            pred = []
            for i in range(0, n):
                open = o[i]
                high = h[i]
                low = l[i]
                output = reg.predict([[open, high, low]])
                pred.append(output)

            pred1 = np.concatenate(pred)
            predicted = pred1.flatten().tolist()

            t = predicted[-1]
            currency_symbol = get_currency_symbol(ticker)
            st.write("  ")
            st.write("  ")
            st.write("  ")
            st.subheader("Your latest predicted closing price is: ")
            st.title(f"{currency_symbol}  {t}")

            st.write("  ")
            st.write("  ")
            st.write("  ")

            r2 = metrics.r2_score(y_test, y_pred)
            mae = metrics.mean_absolute_error(y_test, y_pred)
            mse = metrics.mean_squared_error(y_test, y_pred)
            rmse = mse ** 0.5

            col1, col2 = st.columns(2)

            col1.metric("R2 Score", r2, "± 5%")
            col2.metric("Mean Absolute Error ", mae, "± 5%")
            col1.metric("Mean Squared Error", mse, "± 5%")
            col2.metric("Root Mean Squared Error", rmse, "± 5%")

if __name__ == '__main__':
    main()
