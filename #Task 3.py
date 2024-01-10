#Task 3.2

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
        return unique_tokens_count.most_common(30)
    except Exception as e:
        print(f"Error counting unique tokens: {e}")
        return []

desktop_path = os.path.join(os.path.expanduser("~"), 'Desktop')
txt_file_path = os.path.join(desktop_path, 'CDU', 'SUM Sem 2023', 'Now Software', 'Program 2', 'combined_text.txt')

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
    output_file_path = os.path.join(desktop_path, 'CDU', 'SUM Sem 2023', 'Now Software', 'Program 2', 'top_30_tokens_biobert.txt')
    try:
        with open(output_file_path, 'w', encoding='utf-8') as file:
            for token, count in top_30_tokens:
                file.write(f"{token}: {count}\n")
        print(f'Top 30 tokens saved to {output_file_path}')
    except Exception as e:
        print(f"Error writing output file: {e}")
        exit(1)
