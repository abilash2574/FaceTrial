import numpy as np
import pandas as pd

arr = [[np.arange(1,11)], [np.arange(11,21)], [np.arange(21,31)]]

arrList = ['one', 'two', 'three']
# print(arr)

df = pd.DataFrame(arr, arrList)

print(list(df.index.values.tolist()))

print(df)

df.to_csv(r'encode_data.csv')

