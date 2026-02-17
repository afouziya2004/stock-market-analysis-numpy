import numpy as np

def load_stock_data(file_path):
    data = np.genfromtxt(
        file_path,
        delimiter=",",
        skip_header=1,
        usecols=(1,2,3,4,5)
    )
    return data
