#%%
import pandas as pd
import numpy as np
# %%
data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
       'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
       'Sales':[200,120,340,124,243,350]}
# %%
df=pd.DataFrame(data)
# %%
df
# %%
bycomp=df.groupby('Company')
bycomp.mean()
# %%
bycomp.std()
#%%
bycomp.sum()
# %%
df.groupby('Company').describe().transpose()
# %%
