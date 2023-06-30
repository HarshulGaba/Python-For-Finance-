#%%
import numpy as np
# %%
arr=np.arange(0,11)
arr
# %%
arr[10]
# %%
arr[4:9]
# %%
arr[0:5]=100
arr
# %%
arr=np.arange(0,11)
slice_of_arr=arr[0:5]
slice_of_arr
# %%
slice_of_arr[:]=99
slice_of_arr
# %%
arr
# %%
arr_copy=arr.copy()
arr_copy
# %%
arr_copy[:5]=9
print(arr_copy)
arr
# %%
mat=np.arange(1,11)
mat=mat.reshape(5,2)
# %%
mat[2]
# %%
mat[1,1]
# %%
mat[3,1]
# %%
mat[0:3,1]
# %%
#CONDITIONAL SELECTION
arr=np.arange(1,11)
# %%
arr>4
# %%
bool_arr=arr>4
# %%
arr[bool_arr]
# %%
