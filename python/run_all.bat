@echo off

cd..
cd xampp/htdocs/PROJECT/python

streamlit run stock.py --server.headless true
streamlit run predict.py --server.headless true
streamlit run predict.py --server.headless true
streamlit run aapl.py --server.headless true
streamlit run googl.py --server.headless true
streamlit run amzn.py --server.headless true
streamlit run tsla.py --server.headless true
streamlit run tsla.py --server.headless true
streamlit run reliance.py --server.headless true
streamlit run tcs.py --server.headless true
streamlit run infy.py --server.headless true
streamlit run sbi.py --server.headless true
streamlit run hdfcbank.py --server.headless true
