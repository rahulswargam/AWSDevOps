# Part 1: Extract Data from CSV and Store in NumPy Arrays

import pandas as pd
import numpy as np

# Load the CSV file
df = pd.read_csv('SalaryGender.csv')

# Extract columns into NumPy arrays
salary = df['Salary'].to_numpy()
gender = df['Gender'].to_numpy()
age = df['Age'].to_numpy()
phd = df['PhD'].to_numpy()

salary, gender, age, phd

# Part 2: Find the Number of Men and Women with a PhD

# Count the number of men with a PhD
men_with_phd = df[(df['Gender'] == 'Male') & (df['PhD'] == 1)].shape[0]

# Count the number of women with a PhD
women_with_phd = df[(df['Gender'] == 'Female') & (df['PhD'] == 1)].shape[0]

men_with_phd, women_with_phd


# Part 3: Store "Age" and "PhD" Columns in One DataFrame and Delete Non-PhD Data

# Store "Age" and "PhD" columns in a new DataFrame
age_phd_df = df[['Age', 'PhD']]

# Delete the data of all people who don’t have a PhD
phd_df = df[df['PhD'] == 1]

age_phd_df, phd_df


# Part 4: Calculate the Total Number of People with a PhD

total_phd = df[df['PhD'] == 1].shape[0]
total_phd


# Part 5: Count the Number of Times Each Value Appears in an Array

array = [0, 5, 4, 0, 4, 4, 3, 0, 0, 5, 2, 1, 1, 9]
count = np.bincount(array)
count


# Part 6: Filter Elements Greater Than 5

array = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
filtered_elements = array[array > 5]
filtered_elements


# Part 7: Create and Omit NaN Elements

array = np.array([np.nan, 1, 2, np.nan, 3, 4, 5])
without_nan = array[~np.isnan(array)]
array, without_nan


# Part 8: 10x10 Array with Random Values and Find Min/Max

random_array = np.random.random((10, 10))
min_value = random_array.min()
max_value = random_array.max()
min_value, max_value


# Part 9: Random Vector and Find Mean

random_vector = np.random.random(30)
mean_value = random_vector.mean()
mean_value


# Part 10: Negate Elements Between 3 and 9

array = np.arange(11)
array[(array >= 3) & (array <= 9)] *= -1
array


# Part 11: Sort Random Array by Columns

random_matrix = np.random.random((3, 3))
sorted_by_1st_col = random_matrix[random_matrix[:, 0].argsort()]
sorted_by_2nd_col = random_matrix[random_matrix[:, 1].argsort()]
sorted_by_3rd_col = random_matrix[random_matrix[:, 2].argsort()]

sorted_by_1st_col, sorted_by_2nd_col, sorted_by_3rd_col


# Part 12: Sum Over Last Two Axes

four_d_array = np.random.random((3, 3, 3, 3))
sum_over_last_two = four_d_array.sum(axis=(-1, -2))
sum_over_last_two


# Part 13: Swap Two Rows in a Random Array

random_array = np.random.random((4, 4))
random_array[[0, 1]] = random_array[[1, 0]]
random_array


# Part 14: Compute Matrix Rank

random_matrix = np.random.random((4, 4))
rank = np.linalg.matrix_rank(random_matrix)
rank


# Part 15: School Outcomes Analysis in Tennessee Using Pandas

# Phase 1: Data Collection

# Load the school data
school_data = pd.read_csv('Tennessee_School_Data.csv')

# Describe the data
school_data_description = school_data.describe()
school_data_description


# Phase 2: Group Data by School Ratings

# Group data by school ratings
grouped_data = school_data.groupby('school_rating')['reduced_lunch'].describe()
grouped_data


# Phase 3: Correlation Analysis

# Calculate the correlation
correlation = school_data['reduced_lunch'].corr(school_data['school_rating'])
correlation


# Phase 4: Scatter Plot

import matplotlib.pyplot as plt

# Scatter plot of school_rating vs reduced_lunch
plt.scatter(school_data['reduced_lunch'], school_data['school_rating'])
plt.xlabel('Reduced Lunch')
plt.ylabel('School Rating')
plt.title('School Rating vs Reduced Lunch')
plt.show()


# Phase 5: Correlation Matrix

import seaborn as sns

# Calculate correlation matrix
correlation_matrix = school_data.corr()

# Plot correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Matrix')
plt.show()