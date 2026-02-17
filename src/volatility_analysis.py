import numpy as np
from data_loader import load_stock_data

data = load_stock_data("data/nse_stock_data.csv")
close_price = data[:, 3]

returns = np.diff(close_price) / close_price[:-1]
volatility = np.std(returns)

print("Stock Volatility:", volatility)
