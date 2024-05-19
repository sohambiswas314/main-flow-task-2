import pandas as pd

# Read CSV file into a DataFrame
df = pd.read_csv('your_file.csv')
print(df.head())  # Display the first few rows of the DataFrame


# Write DataFrame to a CSV file
df.to_csv('output_file.csv', index=False)

# Drop rows with any missing values
df.dropna(inplace=True)

# Fill missing values with a specific value, e.g., 0
df.fillna(value=0, inplace=True)

# Fill missing values with the mean of the column
df['column_name'].fillna(df['column_name'].mean(), inplace=True)

# Drop rows with any missing values
df.dropna(inplace=True)

# Fill missing values with a specific value, e.g., 0
df.fillna(value=0, inplace=True)

# Fill missing values with the mean of the column
df['column_name'].fillna(df['column_name'].mean(), inplace=True)

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Filter rows where the value in 'column_name' is greater than a specific value
filtered_df = df[df['column_name'] > value]
print(filtered_df.head())

# Sort DataFrame by 'column_name' in descending order
sorted_df = df.sort_values(by='column_name', ascending=False)
print(sorted_df.head())

# Group by 'column_name' and calculate the mean of each group
grouped_df = df.groupby('column_name').mean()
print(grouped_df.head())

# Group by 'column_name' and calculate specific aggregates
agg_df = df.groupby('column_name').agg({
    'another_column': 'sum',
    'yet_another_column': 'mean'
})
print(agg_df.head())

# Generate descriptive statistics
stats = df.describe()
print(stats)

# Calculate specific statistics
mean_value = df['column_name'].mean()
median_value = df['column_name'].median()
print(f"Mean: {mean_value}, Median: {median_value}")
