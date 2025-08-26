import json
import csv
import os

def convert_json_to_csv(json_file_path, csv_file_path):
    """
    Convert JSON file to CSV format
    """
    try:
        # Read JSON file
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        if not data or not isinstance(data, list):
            print("Error: JSON file is empty or doesn't contain a list")
            return
        
        # Get all unique fields from all objects
        all_fields = set()
        for item in data:
            if isinstance(item, dict):
                all_fields.update(item.keys())
        
        # Convert set to sorted list for consistent column order
        fieldnames = sorted(list(all_fields))
        
        # Write to CSV
        with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            # Write header
            writer.writeheader()
            
            # Write data rows
            for item in data:
                if isinstance(item, dict):
                    # Handle hashtags array by joining with semicolon
                    if 'hashtags' in item and isinstance(item['hashtags'], list):
                        item['hashtags'] = '; '.join(item['hashtags'])
                    
                    # Write row
                    writer.writerow(item)
        
        print(f"Successfully converted {len(data)} records to CSV")
        print(f"CSV file saved as: {csv_file_path}")
        
    except FileNotFoundError:
        print(f"Error: File {json_file_path} not found")
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format - {e}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    # File paths
    json_file = r"c:\Users\zrhrissi\Documents\agents\Agent_Comments_Scrapper\URLs\Lancome_Official_URLs.json"
    csv_file = r"c:\Users\zrhrissi\Documents\agents\Agent_Comments_Scrapper\URLs\Lancome_Official_URLs.csv"
    
    # Convert JSON to CSV
    convert_json_to_csv(json_file, csv_file)

if __name__ == "__main__":
    main()
