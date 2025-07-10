import os
import json
import pandas as pd

print("Script started")

#Below is a path to the folder
folder_path = "."  # Current directory

#Container for data
all_data = []

#Loop through JSON files
for filename in os.listdir(folder_path):
    if filename.endswith(".json"):
        try:
            with open(os.path.join(folder_path, filename), "r", encoding="utf-8") as f:
                content = json.load(f)
                for item in content:
                    item["topic"] = filename.replace(".json", "").replace("-", " ").title()
                    all_data.append(item)
        except Exception as e:
            print(f"Error loading {filename}: {e}")

#Convert to DataFrame
df = pd.DataFrame(all_data)

#Cleanup if needed (ensure column names are clean)
df.rename(columns={
    'question': 'question',
    'answer': 'answer',
    'source': 'source',
    'scholar': 'scholar',
    # Add more if needed
}, inplace=True)

#Save to Excel
output_file = "merged_fatwas.xlsx"
try:
    df.to_excel(output_file, index=False)
    print(f"Merged fatwas saved as '{output_file}'")
except Exception as e:
    print(f"Error saving file: {e}")

#Show files in folder
print("Files currently in folder:", os.listdir())
