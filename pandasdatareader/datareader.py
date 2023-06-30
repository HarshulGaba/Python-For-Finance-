#%%
import pandas_datareader.data as web
import datetime
start=datetime.datetime(2020,1,1)
end=datetime.datetime(2021,7,7)
reliance=web.DataReader('RELIANCE.NS','yahoo',start,end)
#%% 
reliance.head()
# %%
from pandas_datareader.data import Options
reliance_options=Options('RELIANCE','yahoo')