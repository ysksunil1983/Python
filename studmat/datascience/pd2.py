import pandas as pd
from numpy import random
import matplotlib.pyplot as plt
import os
import sys #only needed to determine Python version number
import matplotlib #only needed to determine Matplotlib version number
names = ['Bob','Jessica','Mary','John','Mel']
random.seed(500)
random_names = [names[random.randint(low=0,high=len(names))] for i in range(1000)]
# Print first 10 records
print(random_names[:10])
births = [random.randint(low=0,high=1000) for i in range(1000)]
print(births[:10])
BabyDataSet = list(zip(random_names,births))
print(BabyDataSet[:10])
df = pd.DataFrame(data = BabyDataSet, columns=['Names', 'Births'])
print(df[:10])
df.to_csv('births1880.txt',index=False,header=False)
df = pd.read_csv('births1880.txt')
print(df.info())
print(df.info())
df = pd.read_csv('births1880.txt', header=None)
print(df.info())
print(df.tail())
df = pd.read_csv('births1880.txt', names=['Names','Births'])
print(df.head(5))
os.remove('births1880.txt')
print(df['Names'].unique())
for x in df['Names'].unique():
    print(x)
print(df['Names'].describe())
name = df.groupby('Names')

# Apply the sum function to the groupby object
df = name.sum()
print(df)
Sorted = df.sort_values(['Births'], ascending=False)
print(Sorted.head(1))




    




