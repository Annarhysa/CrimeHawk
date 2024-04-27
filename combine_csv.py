import pandas as pd
import glob
import os

#entering the data directory
os.chdir(r"data")

# Get a list of CSV files in ascending order
csv_files = sorted(glob.glob('*.csv'))

# Read and concatenate the CSV files
combined_df = pd.concat([pd.read_csv(file) for file in csv_files], ignore_index=True)

# Save the combined data to a new CSV file
combined_df.to_csv('combined.csv', index=False)