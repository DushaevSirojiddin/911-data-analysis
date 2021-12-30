import numpy as np
import pandas as pd
import matplotlib.pyplot as plot
import seaborn as sns

df = pd.read_csv("911.csv")
print(df['zip'].value_counts().head(5))
print(df['twp'].value_counts().head(5))
print(df['title'].nunique())
