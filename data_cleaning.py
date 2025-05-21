# capstone_groupxx.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    """Load the bank marketing dataset from a CSV file."""
    df = pd.read_csv(file_path)
    print(f"Data loaded: {df.shape[0]} rows and {df.shape[1]} columns")
    return df

def clean_data(df):
    """Clean the DataFrame by handling missing values and duplicates."""
    initial_shape = df.shape
    df.drop_duplicates(inplace=True)
    print(f"Dropped duplicates: {initial_shape[0] - df.shape[0]} rows removed.")
    
    # Handle missing values (if any)
    missing_values = df.isnull().sum()
    if missing_values.any():
        print("Missing values before cleaning:")
        print(missing_values[missing_values > 0])
        
        # Drop rows with missing values
        df.dropna(inplace=True)
        print(f"Rows with missing values dropped: {initial_shape[0] - df.shape[0]} rows removed.")
    else:
        print("No missing values found.")

    return df

def basic_statistics(df):
    """Return basic statistics of the DataFrame."""
    stats = df.describe(include='all')
    print("Basic Statistics:")
    print(stats)
    return stats

def plot_distribution(df, column):
    """Plot the distribution of a specified column."""
    plt.figure(figsize=(10, 6))
    sns.histplot(df[column], kde=True, bins=30)
    plt.title(f'Distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.grid()
    plt.show()
