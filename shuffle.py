import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('coherent.csv')

# Shuffle the DataFrame
df = df.sample(frac=1).reset_index(drop=True)

# Save the shuffled DataFrame back to a CSV file
df.to_csv('coherent.csv', index=False)