import pandas as pd
import matplotlib.pyplot as plt

print("Reading data from CSV...")
df = pd.read_csv('data.csv')

print("Filling missing values in 'age'...")
df['age'] = df['age'].fillna(df['age'].mean())

print("Saving cleaned data...")
df.to_csv('/app/cleaned_data.csv', index=False)

print("Creating histogram...")
plt.hist(df['age'], bins=5, color='skyblue')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.savefig('/app/age_distribution.png')

print("Pipeline executed successfully!")
