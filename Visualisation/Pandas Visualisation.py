# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %%



# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# import seaborn as sns


# %%
df1=pd.read_csv('df1.csv',index_col=0)


# %%
df1.head()


# %%
df2=pd.read_csv('df2')


# %%
df2.head()


# %%
df1['A'].hist(bins=30)


# %%
df1['A'].plot(kind='hist',bins=30)


# %%
df1['A'].plot.hist(bins=30)


# %%
df2.plot.area(alpha=0.4)


# %%
df2.plot.bar(stacked=2)


# %%
df1['A'].plot.hist(bins=30,ec='black')


# %%
df1.head()
df1.plot.line(df1.index,'B')


# %%



