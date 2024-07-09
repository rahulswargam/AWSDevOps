import pandas as pd
import numpy as np

# Step 1: Read the CSV files
math_scores = pd.read_csv('MathScoreTerm1.csv')
ds_scores = pd.read_csv('DSScoreTerm1.csv')
physics_scores = pd.read_csv('PhysicsScoreTerm1.csv')

# Step 2: Remove the name and ethnicity columns
columns_to_remove = ['Name', 'Ethnicity']
math_scores = math_scores.drop(columns=columns_to_remove)
ds_scores = ds_scores.drop(columns=columns_to_remove)
physics_scores = physics_scores.drop(columns=columns_to_remove)

# Step 3: Fill missing score data with zero
math_scores = math_scores.fillna(0)
ds_scores = ds_scores.fillna(0)
physics_scores = physics_scores.fillna(0)

# Step 4: Merge the three files on 'StudentID'
merged_scores = pd.merge(math_scores, ds_scores, on='StudentID')
merged_scores = pd.merge(merged_scores, physics_scores, on='StudentID')

# Step 5: Change Sex (M/F) column to 1/2
merged_scores['Sex'] = merged_scores['Sex'].map({'M': 1, 'F': 2})

# Step 6: Store the data in a new file – ScoreFinal.csv
merged_scores.to_csv('ScoreFinal.csv', index=False)

print("Data wrangling complete and saved to ScoreFinal.csv")

# Convert ethnicity to numerical values (optional enhancement)
ethnicity_mapping = {eth: idx for idx, eth in enumerate(math_scores['Ethnicity'].unique())}
math_scores['Ethnicity'] = math_scores['Ethnicity'].map(ethnicity_mapping)
ds_scores['Ethnicity'] = ds_scores['Ethnicity'].map(ethnicity_mapping)
physics_scores['Ethnicity'] = physics_scores['Ethnicity'].map(ethnicity_mapping)

# Fill missing scores with the class average (optional enhancement)
math_scores = math_scores.fillna(math_scores.mean())
ds_scores = ds_scores.fillna(ds_scores.mean())
physics_scores = physics_scores.fillna(physics_scores.mean())

