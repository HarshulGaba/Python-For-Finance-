#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# %%
from datetime import datetime
# %%
my_year=2017
my_month=1
my_day=30
my_hour=13
my_minute=30
my_sec=23
# %%
my_date=datetime(my_year,my_month,my_day)
my_date
# %%
my_date_time=datetime(my_year,my_month,my_day,my_hour,my_minute,my_sec)
type(my_date_time)
# %%
my_date_time.day
# %%
my_date_time.month
# %%
first_two=[datetime(2016,1,1),datetime(2016,1,30)]
first_two
# %%
dt_ind=pd.DatetimeIndex(first_two)
dt_ind
# %%
data=np.random.randn(2,2)
data
# %%
cols=['a','b']
# %%
df=pd.DataFrame(data,dt_ind,cols)
df
# %%
df.index.max()
# %%
df['a'].plot()
# %%
