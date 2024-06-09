import streamlit as st
from newsapi import NewsApiClient

# Initialize News API client
newsapi = NewsApiClient(api_key='7560de7d57564e48984e4e0edf180e28')

def get_stock_news(stock_symbol, language='en', page_size=10):
    """Fetch news articles related to the specified stock symbol."""
    query = f'stock {stock_symbol}'
    response = newsapi.get_everything(
        q=query,
        language=language,
        page_size=page_size,
        sort_by='publishedAt'
    )
    articles = response['articles']
    return articles

# Streamlit app
def main():
    st.set_page_config(layout="wide")  # Set layout as wide

    st.title('Stock Market News and Blogs')

    # Input stock symbol
    stock_symbol = st.text_input('Enter a stock symbol (e.g., AAPL, GOOGL):')

    # Select number of articles to display
    num_articles = st.slider('Select number of articles', min_value=1, max_value=100, value=20)

    if st.button('Search'):
        if stock_symbol:
            # Fetch news articles
            articles = get_stock_news(stock_symbol, page_size=num_articles)

            if articles:
                
                for article in articles:
                    st.markdown(
                        f"""
                        <div style="border: 1px solid #ccc; border-radius: 5px; padding: 10px; margin-bottom: 20px;">
                            <h3 style="margin-top: 0;"><a href="{article['url']}" target="_blank" style="color: #007bff; text-decoration: none;">{article['title']}</a></h3>
                            <p style="margin-bottom: 5px;">Source: {article['source']['name']}</p>
                            <p style="margin-bottom: 5px;">Published at: {article['publishedAt']}</p>
                            <p>{article['description']}</p>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
            else:
                st.write(f"No news found for stock symbol {stock_symbol.upper()}.")
        else:
            st.warning('Please enter a stock symbol.')

if __name__ == '__main__':
    main()
