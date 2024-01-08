import csv
import re
from collections import Counter
from transformers import AutoTokenizer

# Function to process a single CSV file
def process_csv(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        return [" ".join(row) for row in reader]

# Function to count top tokens using BERT tokenizer
def count_top_tokens(text, top_n=30):
    tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
    tokens = tokenizer.tokenize(text)
    token_counts = Counter(tokens)
    return token_counts.most_common(top_n)

# Paths to the CSV files
csv_file_paths = [
    r'C:\Users\azali\OneDrive\Desktop\CDU\SUM Sem 2023\Now Software\Program 2\CSV1.csv',
    r'C:\Users\azali\OneDrive\Desktop\CDU\SUM Sem 2023\Now Software\Program 2\CSV2.csv',
    r'C:\Users\azali\OneDrive\Desktop\CDU\SUM Sem 2023\Now Software\Program 2\CSV3.csv',
    r'C:\Users\azali\OneDrive\Desktop\CDU\SUM Sem 2023\Now Software\Program 2\CSV4.csv'
]

# Read and concatenate text from all CSV files
all_text = []
for file_path in csv_file_paths:
    all_text.extend(process_csv(file_path))
combined_text = ' '.join(all_text)

# Write combined text to a file
output_text_file_path = r'C:\Users\azali\OneDrive\Desktop\CDU\SUM Sem 2023\Now Software\Program 2\combined_data.txt'
with open(output_text_file_path, 'w', encoding='utf-8') as file:
    file.write(combined_text)

# Count the occurrences of each word in the combined text
words = re.findall(r'\w+', combined_text.lower())
word_counts = Counter(words)
top_30_words = word_counts.most_common(30)

# Write the top 30 words to a CSV file
output_csv_path = r'C:\Users\azali\OneDrive\Desktop\CDU\SUM Sem 2023\Now Software\Program 2\top_30_words.csv'
with open(output_csv_path, 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Word', 'Count'])
    writer.writerows(top_30_words)

# Get the top 30 tokens using the BERT tokenizer
top_30_tokens = count_top_tokens(combined_text)

# Display the top 30 tokens
for token, count in top_30_tokens:
    print(f"{token}: {count}")
