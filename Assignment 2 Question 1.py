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
    import spacy
from transformers import AutoTokenizer, AutoModelForTokenClassification
import torch
from collections import Counter

# Load spaCy models
nlp_sci = spacy.load('en_core_sci_sm')
nlp_bc5cdr = spacy.load('en_ner_bc5cdr_md')

# Load BioBERT model and tokenizer
biobert_model_name = 'dmis-lab/biobert-base-cased-v1.1'
biobert_tokenizer = AutoTokenizer.from_pretrained(biobert_model_name)
biobert_model = AutoModelForTokenClassification.from_pretrained(biobert_model_name)

# Function to extract entities using spaCy
def extract_entities_spacy(text, model):
    doc = model(text)
    return [(ent.text, ent.label_) for ent in doc.ents]

# Function to extract entities using BioBERT
def extract_entities_biobert(text, tokenizer, model):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
    outputs = model(**inputs)
    predictions = torch.argmax(outputs.logits, dim=2)[0]
    tokens = tokenizer.convert_ids_to_tokens(inputs["input_ids"][0])

    entities = []
    current_entity = ''
    for token, prediction in zip(tokens, predictions):
        if token.startswith("##"):
            current_entity += token[2:]
        else:
            if current_entity:
                entities.append(current_entity)
            current_entity = token if prediction != 0 else ''
    
    if current_entity:
        entities.append(current_entity)

    return entities

# Read the text file
txt_file_path = r'C:\Users\azali\OneDrive\Desktop\CDU\SUM Sem 2023\Now Software\Program 2\combined_text.txt'
with open(txt_file_path, 'r', encoding='utf-8') as file:
    text = file.read() 
# Extract entities using spaCy
entities_spacy = extract_entities_spacy(text, nlp_sci) + extract_entities_spacy(text, nlp_bc5cdr)

# Extract entities using BioBERT
entities_biobert = extract_entities_biobert(text, biobert_tokenizer, biobert_model)

# Convert list of entities to sets for comparison
entities_spacy_set = set([ent[0] for ent in entities_spacy])
entities_biobert_set = set(entities_biobert)

# Compare the results
common_entities = entities_spacy_set.intersection(entities_biobert_set)
diff_spacy_biobert = entities_spacy_set - entities_biobert_set
diff_biobert_spacy = entities_biobert_set - entities_spacy_set

print(f"Total entities detected by spaCy: {len(entities_spacy_set)}")
print(f"Total entities detected by BioBERT: {len(entities_biobert_set)}")
print(f"Common entities: {common_entities}")
print(f"Differences in entities (spaCy - BioBERT): {diff_spacy_biobert}")
print(f"Differences in entities (BioBERT - spaCy): {diff_biobert_spacy}")

# Check for most common words in the text
word_counts = Counter(text.split())
top_10_words = word_counts.most_common(10)
print(f"Top 10 most common words in the text: {top_10_words}")
