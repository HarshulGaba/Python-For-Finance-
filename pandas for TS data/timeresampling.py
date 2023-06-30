#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline
# %%
df=pd.read_csv('walmart_stock.csv')
df
# %%
df.info()
# %%
df['Date']=pd.to_datetime(df['Date'])
df.info()
# %%
df.set_index('Date',inplace=True)
# %%
df.head()
# %%
df1=pd.read_csv('walmart_stock.csv',index_col='Date',parse_dates=True)
# %%
df1.head()
# %%
df.resample(rule='Q').var()
# %%
df['Close'].resample(rule='M').mean().plot.bar(ec='black',figsize=(12,3))
# %%
