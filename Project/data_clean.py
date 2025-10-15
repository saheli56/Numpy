# importing necessary libraries
import pandas as pd
import numpy as np

#loading the dataset
df = pd.read_csv('C:/Numpy/project/Messy_Employment_India_Dataset.csv')
print(df.head())
#checking the missing values
print('Missing values in each column:')
print(df.isnull().sum())

#filling missing values with the mean of the column
df['status'].fillna(df['status'].mode()[0], inplace=True)
df['Age Group'].fillna(df['Age Group'].mode()[0], inplace=True)
df['Education'].fillna(df['Education'].mode()[0], inplace=True)
df['Industry'].fillna(df['Industry'].mode()[0], inplace=True)
df['Location'].fillna(df['Location'].mode()[0], inplace=True)
df['AI Risk'].fillna(df['AI Risk'].mode()[0], inplace=True)
df['Monthly Salary (INR)'].fillna(df['Monthly Salary (INR)'].mean(), inplace=True)
df['Years of Experience'].fillna(df['Years of Experience'].median(), inplace=True)

#replace the infinety values with NaN
df.replace({np.inf: np.nan, -np.inf: np.nan}, inplace=True)
df.fillna(df.mean(), inplace=True)

#remove the duplicates
df.drop_duplicates(inplace=True)