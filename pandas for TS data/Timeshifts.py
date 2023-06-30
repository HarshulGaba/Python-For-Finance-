#%%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
%matplotlib inline
# %%
df=pd.read_csv('walmart_stock.csv',index_col='Date',parse_dates=True)
df
