# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %%
import pandas as pd
import matplotlib.pyplot as plt
# %%
airline=pd.read_csv('airline_passengers.csv')
airline.dropna(inplace=True)


# %%
airline.set_index('Month')


# %%
airline.index=pd.to_datetime(airline.index)


# %%
from statsmodels.tsa.seasonal import seasonal_decompose


# %%
result=seasonal_decompose(airline['Thousands of Passengers'],model='multiplicative')


# %%



