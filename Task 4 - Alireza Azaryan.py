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
