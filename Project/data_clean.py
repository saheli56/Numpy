# importing necessary libraries
import pandas as pd
import numpy as np

#loading the dataset
df = pd.read_csv('C:/Numpy/project/Messy_Employment_India_Dataset.csv')
print(df.head())
#checking the missing values
print('Missing values in each column:')
print(df.isnull().sum())