import pandas as pd
import re

# Path to the input CSV file containing the data
input_csv_file_path = "C:/Users/USER/Desktop/Reviews.csv"

# Path to the output CSV file to save the cleaned data
output_csv_file_path = "C:/Users/USER/Desktop/Reviews3.csv"

# Read the CSV file into a pandas DataFrame
data = pd.read_csv(input_csv_file_path)

# Define a function to clean text by removing symbols and numbers
def clean_text(text):
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text)  # Remove symbols
    cleaned_text = re.sub(r'\d', '', cleaned_text)   # Remove numbers
    return cleaned_text

# Apply the clean_text function to the 'Text' column
data['Text'] = data['Text'].apply(clean_text)

# Keep only the 'Text' column and drop the rest
data = data[['Text']]

# Save the cleaned DataFrame to a new CSV file
data.to_csv(output_csv_file_path, index=False)

print(f"Cleaned data saved to: {output_csv_file_path}")
