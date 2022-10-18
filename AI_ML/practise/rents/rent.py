import pandas as pd
filepath='melb_data.csv'
data = pd.read_csv(filepath)
print(data.describe())
print("-------------------------------------------------------------------------")
print(data)