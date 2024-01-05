import csv

# Paths to the CSV files
csv_file_paths = [
    'C:\Users\azali\OneDrive\Desktop\CDU\SUM Sem 2023\Now Software\Program 2\CSV1.csv',
    'C:\Users\azali\OneDrive\Desktop\CDU\SUM Sem 2023\Now Software\Program 2\CSV2.csv',
    'C:\Users\azali\OneDrive\Desktop\CDU\SUM Sem 2023\Now Software\Program 2\CSV3.csv',
    'C:\Users\azali\OneDrive\Desktop\CDU\SUM Sem 2023\Now Software\Program 2\CSV4.csv'
]

# Initialize an empty list to store all text
all_text = []

# Function to process a single CSV file
def process_csv(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        # Join each row's content with a comma and collect all rows in a list
        return [" ".join(row) for row in reader]

# Loop through each CSV file path
for file_path in csv_file_paths:
    csv_content = process_csv(file_path)
    all_text.append(f"===== Begin {file_path} =====\n")
    all_text.append("\n".join(csv_content))
    all_text.append(f"\n===== End {file_path} =====\n")

# Path to the output text file
output_text_file_path = r'C:\Users\azali\OneDrive\Desktop\CDU\SUM Sem 2023\Now Software\Program 2\combined_data.txt'

# Write all the text to the output file
with open(output_text_file_path, 'w', encoding='utf-8') as file:
    file.write("\n".join(all_text))

print(f"Data extracted from all CSV files into {output_text_file_path}")






import re
from collections import Counter
import csv

# Path to the text file
text_file_path = r'C:\Users\azali\OneDrive\Desktop\CDU\SUM Sem 2023\Now Software\Program 2\combined_data.txt'

# Read the text file
with open(text_file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# Use regular expression to extract words from the text
words = re.findall(r'\w+', text.lower())

# Count the occurrences of each word
word_counts = Counter(words)

# Get the 'Top 30' most common words
top_30_words = word_counts.most_common(30)

# Path to the output CSV file
output_csv_path = r'C:\Users\azali\OneDrive\Desktop\CDU\SUM Sem 2023\Now Software\Program 2\top_30_words.csv'

# Write the 'Top 30' common words and their counts to a CSV file
with open(output_csv_path, 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Word', 'Count'])  # Writing the header
    writer.writerows(top_30_words)

print(f"Top 30 common words and their counts are stored in {output_csv_path}")

import transformers
from collections import Counter

def count_top_tokens(text_path, top_n=30):
    # Initialize the tokenizer
    tokenizer = transformers.AutoTokenizer.from_pretrained("bert-base-uncased")

    # Read the text file
    with open(text_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Tokenize the text
    tokens = tokenizer.tokenize(text)

    # Count the occurrences of each token
    token_counts = Counter(tokens)

    # Get the top 'n' tokens
    top_tokens = token_counts.most_common(top_n)

    return top_tokens

# Path to the text file
text_file_path = r'C:\Users\azali\OneDrive\Desktop\CDU\SUM Sem 2023\Now Software\Program 2\combined_data.txt'

# Get the top 30 tokens
top_30_tokens = count_top_tokens(text_file_path)

# Display the top 30 tokens
for token, count in top_30_tokens:
    print(f"{token}: {count}")
