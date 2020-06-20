import pandas as pd

pos_count = 100
neg_count = 90

df2 = pd.DataFrame({"Positive": [pos_count], "Negative": [neg_count]})

print(df2)

import numpy as np

numpy_df = df2.values
print(numpy_df)

import matplotlib.pyplot as plt