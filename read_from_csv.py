import pandas as pd
import numpy as np

df = pd.read_csv(r'encode_data.csv', index_col=0)

print(df)

print(list(df.index.values.tolist()))