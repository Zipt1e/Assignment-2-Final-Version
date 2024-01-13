import spacy

# Load SpaCy models
nlp_sci_sm = spacy.load("en_core_sci_sm")
nlp_bc5cdr_md = spacy.load("en_ner_bc5cdr_md")

def extract_entities_spacy(text, model):
    doc = model(text)
    return [(ent.text, ent.label_) for ent in doc.ents]

text_file_path = r'C:\Users\azali\OneDrive\Desktop\CDU\SUM Sem 2023\Now Software\Program 2\combined_text.txt'

with open(text_file_path, 'r', encoding='utf-8') as file:
    text = file.read()

entities_sci_sm = extract_entities_spacy(text, nlp_sci_sm)
entities_bc5cdr_md = extract_entities_spacy(text, nlp_bc5cdr_md)

from collections import Counter

# Count entities from each model
counter_sci_sm = Counter([ent[0] for ent in entities_sci_sm])
counter_bc5cdr_md = Counter([ent[0] for ent in entities_bc5cdr_md])

print("Entities from en_core_sci_sm:", counter_sci_sm)
print("Entities from en_ner_bc5cdr_md:", counter_bc5cdr_md)
 