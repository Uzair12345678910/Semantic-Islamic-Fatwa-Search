import pandas as pd
from sentence_transformers import InputExample
import pickle

# Load the Excel dataset
df = pd.read_excel("merged_fatwas.xlsx")  # Replace with your actual filename

# Remove any rows with missing data
df.dropna(subset=["question", "answer"], inplace=True)

# Prepare positive pairs
train_examples = [
    InputExample(texts=[row["question"], row["answer"]], label=1.0)
    for _, row in df.iterrows()
]

# Save to a file (optional but helpful for training later)
with open("fatwa_train_examples.pkl", "wb") as f:
    pickle.dump(train_examples, f)

print(f"✅ Created {len(train_examples)} training examples.")
