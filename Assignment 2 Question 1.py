#Task 1

import os
import csv

# Paths to the CSV files
csv_file_paths = [
    r'C:\Users\azali\OneDrive\Desktop\CDU\SUM Sem 2023\Now Software\Program 2\CSV1.csv',
    r'C:\Users\azali\OneDrive\Desktop\CDU\SUM Sem 2023\Now Software\Program 2\CSV2.csv',
    r'C:\Users\azali\OneDrive\Desktop\CDU\SUM Sem 2023\Now Software\Program 2\CSV3.csv',
    r'C:\Users\azali\OneDrive\Desktop\CDU\SUM Sem 2023\Now Software\Program 2\CSV4.csv'
]

all_texts = []

for file_path in csv_file_paths:
    if os.path.isfile(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            headers = next(reader)
            max_text_column = max(range(len(headers)), key=lambda i: sum(len(row[i]) for row in reader))
            file.seek(0)
            next(reader)  # Skip header line
            all_texts.extend(row[max_text_column].strip() for row in reader if len(row) > max_text_column)
    else:
        print(f"File '{file_path}' not found. Skipping.")

# Writing all extracted text to a new file
output_txt_path = r'C:\Users\azali\OneDrive\Desktop\CDU\SUM Sem 2023\Now Software\Program 2\combined_text.txt'
with open(output_txt_path, 'w', encoding='utf-8') as file:
    file.write('\n'.join(all_texts))
print(f'Combined txt Built saved to {output_txt_path}')

#Task 3.1
from collections import Counter

txt_file_path = r'C:\Users\azali\OneDrive\Desktop\CDU\SUM Sem 2023\Now Software\Program 2\combined_text.txt'

with open(txt_file_path, 'r', encoding='utf-8') as file:
    words = file.read().split()
word_counts = Counter(words)
top_30_words = word_counts.most_common(30)

csv_file_path = r'C:\Users\azali\OneDrive\Desktop\CDU\SUM Sem 2023\Now Software\Program 2\top_30_words.csv'

with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Word', 'Count'])
    csv_writer.writerows(top_30_words)

print(f'Top 30 words and counts saved to {csv_file_path}')

# Task 3.2
from transformers import AutoTokenizer
from collections import Counter

biobert_model_name = 'dmis-lab/biobert-base-cased-v1.1'

try:
    tokenizer = AutoTokenizer.from_pretrained(biobert_model_name)
except Exception as e:
    print(f"Error initializing tokenizer: {e}")
    exit(1)

def count_unique_tokens(text):
    tokens = tokenizer.tokenize(text)
    return Counter(tokens).most_common(30)

txt_file_path = r'C:\Users\azali\OneDrive\Desktop\CDU\SUM Sem 2023\Now Software\Program 2\combined_text.txt'

try:
    with open(txt_file_path, 'r', encoding='utf-8') as file:
        combined_text = file.read()
    top_30_tokens = count_unique_tokens(combined_text)
except Exception as e:
    print(f"Error processing text file: {e}")
    exit(1)

output_file_path = r'C:\Users\azali\OneDrive\Desktop\CDU\SUM Sem 2023\Now Software\Program 2\top_30_tokens_biobert.txt'
try:
    with open(output_file_path, 'w', encoding='utf-8') as file:
        for token, count in top_30_tokens:
            file.write(f"{token}: {count}\n")
    print(f'Top 30 tokens saved to {output_file_path}')
except Exception as e:
    print(f"Error writing output file: {e}")
    exit(1)


# Task 4
    txt_file_path = r'C:\Users\azali\OneDrive\Desktop\CDU\SUM Sem 2023\Now Software\Program 2\combined_text.txt'

with open(txt_file_path, 'r', encoding='utf-8') as file:
    text = file.read()

import spacy

# Load the Spacy model
# Choose either 'en_core_sci_sm' or 'en_ner_bc5cdr_md' based on availability and requirement
nlp = spacy.load('en_core_sci_sm')  # or 'en_ner_bc5cdr_md'

doc = nlp(text)

# Extract 'diseases' and 'drugs' entities
entities_spacy = [(ent.text, ent.label_) for ent in doc.ents if ent.label_ in ['DISEASE', 'CHEMICAL']]

from collections import Counter

# Example: Counting entities
entities_count_spacy = Counter([label for _, label in entities_spacy])

# You would do similar processing for the BioBERT extracted entities

# Then you can compare these counts and the specific entities extracted by each model
