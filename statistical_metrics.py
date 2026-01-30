import numpy as np
from data_loader import load_stock_data

data = load_stock_data("data/nse_stock_data.csv")
close_price = data[:, 3]

print("Mean Close Price:", np.mean(close_price))
print("Median Close Price:", np.median(close_price))
print("Variance:", np.var(close_price))
print("Standard Deviation:", np.std(close_price))
