import numpy as np
import pandas as pd
import matplotlib.pyplot as plot
import seaborn as sns

df = pd.read_csv('911.csv')
apply = lambda x: x.split(':')[0]
df = df.assign(Reason=df['title'].apply(apply))
print(df['Reason'].value_counts())
sns.countplot(x='Reason', data=df, palette='viridis')
plot.show()
print(type(df['timeStamp'].iloc[0]))

df['timeStamp'] = pd.to_datetime(df['timeStamp'], format='%Y-%m-%d %H:%M:%S')
print(df['timeStamp'].iloc[0].hour)

df['Hour'] = df['timeStamp'].apply(lambda x: x.hour)
df['Month'] = df['timeStamp'].apply(lambda x: x.month)
df['Day of Week'] = df['timeStamp'].apply(lambda x: x.dayofweek)

print(df.head())

