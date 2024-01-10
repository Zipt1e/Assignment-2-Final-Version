# Question 1
# Task 1

import os

csv_files = ['CSV1.csv', 'CSV2.csv', 'CSV3.csv', 'CSV4.csv']

desktop_path = os.path.join(os.path.expanduser("~"), 'Desktop')

folder_path = os.path.join(desktop_path, 'Software Now', 'Task 1')

output_txt_path = os.path.join(desktop_path, 'Software Now', 'Task 1', 'output', 'all_text.txt')

all_texts = []

for file_name in csv_files:
    file_path = os.path.join(folder_path, file_name)

    if os.path.isfile(file_path): 
        with open(file_path, 'r', encoding='utf-8') as file:
            max_text_column = None
            max_text_length = 0

            headers = file.readline().strip().split(',')

            for column_name in headers:
                file.seek(0)

                next(file)

                text_length = sum(len(row.split(',')[headers.index(column_name)].strip()) if len(row.split(',')) > headers.index(column_name) else 0 for row in file)

                if text_length > max_text_length:
                    max_text_column = column_name
                    max_text_length = text_length

            file.seek(0)
            next(file)
            all_texts.extend(row.split(',')[headers.index(max_text_column)].strip() if len(row.split(',')) > headers.index(max_text_column) else '' for row in file)

    else:
        print(f"File '{file_name}' not found. Skipping.")

combined_text = '\n'.join(all_texts)

with open(output_txt_path, 'w', encoding='utf-8') as file:
    file.write(combined_text)


# Task 3.1


import csv
from collections import Counter

txt_file_path = '/Users/justincooper/Desktop/Software Now/Task 1/output/all_text.txt'

with open(txt_file_path, 'r', encoding='utf-8') as file:
    text = file.read()

words = text.split()

word_counts = Counter(words)

top_30_words = word_counts.most_common(30)

csv_file_path = '/Users/justincooper/Desktop/Software Now/Task 1/output/top_30_words.csv'

with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    
    csv_writer.writerow(['Word', 'Count'])
    
    csv_writer.writerows(top_30_words)

print(f'Top 30 words and counts saved to {csv_file_path}')



# Task 3.2
        

from transformers import AutoTokenizer
from collections import Counter
import os

biobert_model_name = 'dmis-lab/biobert-base-cased-v1.1'

try:
    tokenizer = AutoTokenizer.from_pretrained(biobert_model_name)
except Exception as e:
    print(f"Error initializing tokenizer: {e}")
    exit(1)

def count_unique_tokens(text):
    try:
        tokens = tokenizer.tokenize(tokenizer.decode(tokenizer.encode(text)))
        unique_tokens_count = Counter(tokens)
        top_30_tokens = unique_tokens_count.most_common(30)
        return top_30_tokens
    except Exception as e:
        print(f"Error counting unique tokens: {e}")
        return []

desktop_path = os.path.join(os.path.expanduser("~"), 'Desktop')
txt_file_path = os.path.join(desktop_path, 'Software Now', 'Task 1', 'output', 'all_text.txt')

try:
    with open(txt_file_path, 'r', encoding='utf-8') as file:
        combined_text = file.read()
except Exception as e:
    print(f"Error reading text file: {e}")
    exit(1)

top_30_tokens = count_unique_tokens(combined_text)

if not top_30_tokens:
    print("No unique tokens found. Check for potential errors.")
else:
    output_file_path = os.path.join(desktop_path, 'Software Now', 'Task 1', 'output', 'top_30_tokens_biobert.txt')
    try:
        with open(output_file_path, 'w', encoding='utf-8') as file:
            for token, count in top_30_tokens:
                file.write(f"{token}: {count}\n")
        print(f'Top 30 tokens saved to {output_file_path}')
    except Exception as e:
        print(f"Error writing output file: {e}")
        exit(1)
