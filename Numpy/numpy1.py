# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as np


# %%
my_list=[1,2,3]
x=np.array(my_list)


# %%
my_matrix=[[1,2,3],[1,4,5],[6,7,8]]
matrix=np.array(my_matrix)
matrix


# %%
list(range(0,5))


# %%
np.arange(0,5)


# %%
np.zeros(3)


# %%
np.zeros([3,30])


# %%
np.ones((5,5))


# %%
np.linspace(0,49,50)


# %%
np.eye(5)


# %%
np.random.rand(5,4)


# %%
np.random.randn(5,4)


# %%
np.random.randint(0,100,10)
# %%

# %%
arr=np.random.randint(1,101,10)
arr1=np.arange(0,25)
# %%
arr1.reshape(5,5)
# %%
arr1.reshape(5,5).shape
# %%
arr1.dtype
# %%
arr
# %%
arr.max()
# %%
arr.argmax()
# %%
arr.argmin()
# %%
arr.shape[0]
# %%
