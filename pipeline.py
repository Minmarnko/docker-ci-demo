import pandas as pd
import matplotlib.pyplot as plt

# Load data from the CSV file
df = pd.read_csv('data.csv')

# Fill missing values in 'age' with the mean of the column
df['age'] = df['age'].fillna(df['age'].mean())

# Save the cleaned data into a new CSV file
df.to_csv('/app/cleaned_data.csv', index=False)

# Create a histogram of the 'age' column and save it as a PNG file
plt.hist(df['age'], bins=5, color='skyblue')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.savefig('/app/age_distribution.png')
