import json
import pandas as pd
import zipfile
import os
import logging

# Function to load JSON files from a zip archive
def load_json_from_zip(zip_path):
    data = []
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        for file_name in zip_ref.namelist():
            with zip_ref.open(file_name) as file:
                json_data = json.load(file)
                if isinstance(json_data, dict):
                    data.append(json_data)
                elif isinstance(json_data, list):
                    for item in json_data:
                        if isinstance(item, dict):
                            data.append(item)
                        else:
                            logging.warning(f"Skipping non-dictionary item of type {type(item)} in list in file {file_name}")
                else:
                    logging.warning(f"Skipping non-dictionary or non-list item of type {type(json_data)} in file {file_name}")
    return data

# Directory containing the zip files
eval_results_dir = 'eval_results'

# List all zip files in the directory
zip_files = [f for f in os.listdir(eval_results_dir) if f.endswith('.zip')]

# Combine all data into a single DataFrame
all_data = []
for zip_file in zip_files:
    zip_path = os.path.join(eval_results_dir, zip_file)
    data = load_json_from_zip(zip_path)
    for item in data:
        df = pd.DataFrame(item)
        model_name = os.path.splitext(zip_file)[0].split('_')[2]
        df['model'] = model_name
        all_data.append(df)

# Combine all DataFrames into a single DataFrame
combined_df = pd.concat(all_data, ignore_index=True)

# Ensure 'question' and 'answer' columns exist
if 'question' not in combined_df.columns or 'answer' not in combined_df.columns:
    raise ValueError("The data must contain 'question' and 'answer' columns")

# Create a pivot table with questions as rows and models as columns
pivot_df = combined_df.pivot_table(
    index='question', 
    columns='model', 
    values='pred', 
    aggfunc=lambda x: (x == combined_df.loc[x.index, 'answer']).astype(int).max(), 
    fill_value=0
)

# Save the pivot table to a CSV file
pivot_df.to_csv('model_performance.csv')
