import yfinance as yf

data =yf.download("TSLA",period="5y",multi_level_index=False)
print(data)