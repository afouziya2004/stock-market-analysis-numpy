import numpy as np
from data_loader import load_stock_data

data = load_stock_data("data/nse_stock_data.csv")

open_price = data[:, 0]
close_price = data[:, 3]

daily_returns = (close_price[1:] - close_price[:-1]) / close_price[:-1]

print("Daily Returns:")
print(daily_returns)
