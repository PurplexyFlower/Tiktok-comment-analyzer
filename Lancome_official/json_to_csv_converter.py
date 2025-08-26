import json
import csv
import pandas as pd

def convert_json_to_csv_sample(json_file_path, csv_file_path, sample_size=10):
    """
    Convert a sample of entries from JSON file to CSV format
    """
    try:
        # Read the JSON file
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        print(f"Total entries in JSON: {len(data)}")
        print(f"Taking sample of {sample_size} entries")
        
        # Take a sample of entries
        sample_data = data[:sample_size]
        
        # Convert to DataFrame for easier handling
        df = pd.json_normalize(sample_data)
        
        # Save to CSV
        df.to_csv(csv_file_path, index=False, encoding='utf-8')
        
        print(f"Successfully converted {len(sample_data)} entries to CSV")
        print(f"CSV file saved as: {csv_file_path}")
        
        # Display the first few rows
        print("\nFirst few rows of the CSV:")
        print(df.head())
        
        # Display column names
        print(f"\nColumns in CSV: {list(df.columns)}")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    json_file = "lancome.official_data.json"
    csv_file = "lancome_sample_10.csv"
    
    convert_json_to_csv_sample(json_file, csv_file, sample_size=10)
