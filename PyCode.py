import pandas as pd
import time

# Read the CSV file into a pandas DataFrame
csv_file_path = 'Reviews3.csv'  # Replace with the actual path to the CSV file
data = pd.read_csv(csv_file_path)

# Create an empty dictionary to store word counts
word_counts = {}

# Start measuring processing time
start_time = time.time()

# Iterate through each row in the 'Text' column
for text in data['Text']:
    # Split the text into words
    words = text.split()
    
    # Count the instances of each word
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

# Calculate processing time
end_time = time.time()
processing_time = end_time - start_time

print(f"Processing time: {processing_time:.4f} seconds")
