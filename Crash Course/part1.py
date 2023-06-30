# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
1+2
# %%
1-3
# %%
2**4
# %%
'Hi! my name is..'


# %%
x='hello'
print(x)


# %%
print('hello')


# %%
name='Harshul'
print('My name is {}'.format(name))


# %%
name='Harshul'
age=18
subject='PFAT'
print('Age is {1}\nName is {0}\nSubject is {2}'.format(name,age,subject))


# %%
#List
[0,1,2]


# %%
['hi',0,1]


# %%
my_list=[0,1,2]


# %%
my_list.extend([3,4])
print(my_list)


# %%
my_list.append(5)
print(my_list)


# %%
my_list[0]


# %%
my_list[-1]


# %%
my_list[0:4]


# %%
my_list[0:2]


# %%
my_list[3:]


# %%
nested=[0,1,[2,3]]


# %%
nested


# %%
nested[2][0]


# %%
nested[0]


# %%
#dictionaries 
d={'key':10,'key2':'seconditem'}


# %%
d['key2']


# %%
#tuples
tuples=(1,2,3)
tuples[0]


# %%
my_list[0]='watermelon'
my_list


# %%
# tuples[0]='watermelon'


# %%
#set
{1,2,3,4,5}


# %%
set([1,1,2,3,3,2,2,2,4,4,5,5,6,6,6,4])


# %%
import math
math.sqrt(100)


# %%
y='hellooo'
y[0]


# %%
#comparison operators
# %%
1<2
# %%
1>=4
# %%
1=='2'
# %%
1!=1
# %%
(1==2)and(1==1)
# %%
([1,2]==1)
# %%
([1,2][0]==1)
# %%
if (1!=2):
    print('hello')
# %%
#for loops
seq=[0,1,2]
for item in seq:
    print(item)
# %%
seq=['hi','hello','bye']
for words in seq:
    print(words)
# %%
dictionary={'key':20,'key2':30,'key3':40,'key4':50}
for things in dictionary:
    print(dictionary[things])
# %%
#while luups
i=1
while i<5:
    print('i is currently {}'.format(i))
    i+=1
# %%
#range
range(5)
# %%
for i in range(0,5,2):
    print(i)
# %%
#list comprehension
x=[0,1,2,3]
# %%
out=[]
for i in x:
    out.append(i**2)
out
# %%
#list comprehension
out=[i**2 for i in x]
out
# %%
def  my_func(p=1):
    """Doc string idhar likh!"""
    print(p)
my_func(5)
# %%
def new_func(p='enter an argument'):
    return p*5
x=new_func(8)
x
# %%
#lambda expression 
lambda new_fun:new_fun*5
# %%
seq=[1,2,3,4,5]
list(map(new_func,seq))
# %%
seq=[0,1,2,3,4,5]
list(map(lambda new_fun:new_fun*5,seq))
# %%
def is_even(p):
    return p%2==0
list(filter(is_even,seq))
# %%
list(filter(lambda is_even:is_even%2==0,seq))
# %%
#methods
st='Hello hum CBI se hai'
st.lower()
# %%
st.upper()
# %%
tweet='Chalen ghoomne? Bolo'
tweet.split()
# %%
tweet.split('?')[1]
# %%
dictionary
# %%
dictionary.keys()
# %%
dictionary.items()
# %%
my_list
# %%
my_list
# %%
my_list.pop(0)
# %%
my_list
# %%
