@echo off
start "" /B streamlit run stock.py --server.headless true --server.port 8501
start "" /B streamlit run predict.py --server.headless true --server.port 8502
start "" /B streamlit run explore.py --server.headless true --server.port 8503
start "" /B streamlit run aapl.py --server.headless true --server.port 8504
start "" /B streamlit run googl.py --server.headless true --server.port 8505
start "" /B streamlit run amzn.py --server.headless true --server.port 8506
start "" /B streamlit run tsla.py --server.headless true --server.port 8507
start "" /B streamlit run msft.py --server.headless true --server.port 8508
start "" /B streamlit run reliance.py --server.headless true --server.port 8509
start "" /B streamlit run tcs.py --server.headless true --server.port 8510
start "" /B streamlit run infy.py --server.headless true --server.port 8511
start "" /B streamlit run sbi.py --server.headless true --server.port 8512
start "" /B streamlit run hdfcbank.py --server.headless true --server.port 8513
pause
