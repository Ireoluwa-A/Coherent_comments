import pandas as pd

# Load the original CSV file into a DataFrame
df = pd.read_csv('coherent.csv')

# Calculate the indices for splitting
ten = int(len(df) * 0.1)
twenty = ten * 2
# split_index2 = int(len(df) * 0.8)


# Slice the DataFrame into one-third and two-thirds
test_df = df.iloc[:twenty]
dev_df = df.iloc[twenty:twenty + ten]
train_df = df.iloc[twenty + ten:]

# Save the DataFrames to separate CSV files
test_df.to_csv('comment-test.csv', index=False)
dev_df.to_csv('comment-dev.csv', index=False)
train_df.to_csv('comment-train.csv', index=False)
print("Data successfully split.")