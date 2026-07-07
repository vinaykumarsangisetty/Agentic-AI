# Lab 1A — Text Preprocessing Pipeline

**Module:** 1 — NLP Fundamentals  
**Difficulty:** Beginner  
**Duration:** 45 minutes  
**What you'll build:** A Python script that cleans clinical discharge summaries and compares keyword quality across three preprocessing methods.

---

## Why This Matters

In healthcare, physician notes contain abbreviations (`Pt`, `Dx`, `Hx`), drug names, timestamps, and junk characters. Before any AI model reads these notes, you must clean them. Poor preprocessing leads to wrong billing codes, missed diagnoses in search results, and model confusion.

This lab shows you the full pipeline: raw text → tokenized → stopwords removed → stemmed OR lemmatized → keywords extracted.

---

## Learning Objectives

By the end of this lab you will be able to:
1. Tokenize, lowercase, and clean text using NLTK.
2. Explain the difference between stemming and lemmatization.
3. Extract top keywords using TF-IDF.
4. Compare keyword quality across preprocessing methods.

---

## Prerequisites

Make sure you have run the Module 1 environment setup. Then, in your Python session, download NLTK data:

```python
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')
```

---

## Dataset

You will use 15 fictional clinical discharge summaries. These are embedded directly in the code below — no file download required.

---

## Setup: Create Your Notebook

1. Open VS Code (or Jupyter Lab).
2. Create a new file named `lab1a_preprocessing.py` (or a Jupyter notebook `lab1a_preprocessing.ipynb`).
3. Follow the steps below, copying each code block in order.

---

## Step 1 — Import Libraries

Type (or paste) the following at the top of your file:

```python
import pandas as pd
import nltk
import spacy
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

# Download NLTK data (run once)
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

print("Libraries loaded successfully.")
```

**Run this cell.** You should see: `Libraries loaded successfully.`

If you get `ModuleNotFoundError`, go back and run `pip install nltk spacy scikit-learn pandas` in your terminal.

---

## Step 2 — Load the Dataset

Copy this entire block. It creates a pandas DataFrame with 15 discharge summaries:

```python
discharge_summaries = [
    "Pt is a 67-year-old M w/ Hx of T2DM and HTN admitted for chest pain. "
    "ECG showed no ST elevation. Troponin negative x2. Discharged on Metformin 500mg BD and Lisinopril 10mg OD. "
    "Follow-up with cardiologist in 2 wks.",

    "45F presented to ER w/ acute SOB and productive cough x5 days. "
    "CXR revealed RLL consolidation consistent with CAP. "
    "Started on Amoxicillin-Clavulanate 875mg BID. O2 sat improved to 98%. Discharged in stable condition.",

    "72M w/ known CKD Stage 3 and BPH admitted for AKI. "
    "Creatinine peaked at 3.2 mg/dL. IV fluids administered. Nephrology consult obtained. "
    "Medications reviewed: NSAIDs discontinued. Diet counseling provided.",

    "Pt is 55F with h/o depression and anxiety. Presented with worsening mood, insomnia, and decreased appetite x3 weeks. "
    "PHQ-9 score 18 (severe). Started on Sertraline 50mg OD. Referred to outpatient psychiatry.",

    "28M, no significant PMH. Admitted after MVA. GCS 15. CT head negative for intracranial hemorrhage. "
    "Cervical spine cleared. Discharged with analgesia and soft collar. Neurology follow-up arranged.",

    "80F w/ AF on Warfarin presented with INR of 6.2 and minor gum bleeding. "
    "Warfarin held. Vitamin K 2mg PO administered. Repeat INR 2.8 after 48 hours. "
    "Warfarin restarted at reduced dose of 3mg. Hematology follow-up in 1 week.",

    "34M with T1DM admitted for DKA. pH 7.18, glucose 480 mg/dL, ketones large. "
    "IV insulin infusion started. Electrolytes monitored q2h. Transitioned to SC insulin after ketones cleared. "
    "Diabetes education session completed prior to discharge.",

    "61F post CABG Day 3. Wound healing well, no signs of infection. "
    "Cardiac rehab initiated. Discharged on aspirin, atorvastatin, metoprolol, and clopidogrel. "
    "Surgeon review in 2 wks. Diet: low sodium, low fat.",

    "Pt is 50M chronic smoker admitted w/ COPD exacerbation. "
    "FEV1 45% predicted. Nebulized salbutamol and ipratropium given. "
    "Systemic corticosteroids prescribed for 5 days. Smoking cessation counseling offered.",

    "22F admitted for appendicitis. Underwent laparoscopic appendectomy without complications. "
    "Post-op day 2: tolerating oral fluids. Discharged on paracetamol and ibuprofen PRN. "
    "Wound check in 7 days. Activity restriction for 2 weeks.",

    "68M w/ Stage IIIA NSCLC. Admitted for Cycle 2 of carboplatin-pemetrexed chemotherapy. "
    "Tolerated infusion well. Mild nausea managed with ondansetron. CBC reviewed: ANC 1800. "
    "Hydration maintained. Next cycle in 21 days pending CBC results.",

    "77F admitted with confusion and urinary symptoms. MSU confirmed E. coli UTI. "
    "Trimethoprim-Sulfamethoxazole started. Mental status improved within 48h. "
    "MMSE on discharge 24/30. Advised increased fluid intake.",

    "40M w/ psoriatic arthritis on methotrexate. Admitted for elevated LFTs. "
    "Methotrexate held. LFTs trended down over 5 days. Rheumatology review scheduled. "
    "Folic acid supplementation reinforced. Alcohol counseling provided.",

    "56F with fibromyalgia and chronic fatigue syndrome. Admitted for acute pain flare. "
    "Gabapentin dose increased to 600mg TID. PT/OT consult obtained. "
    "CBT referral made. Discharged with written pain management plan.",

    "Neonate, 4 days old, born at 36 wks gestation. Admitted for jaundice. "
    "Bilirubin 18 mg/dL. Phototherapy initiated. Bilirubin trended down to 11 after 24h. "
    "Feeding well on breast milk. Discharged with follow-up at 48h.",
]

df = pd.DataFrame({
    'doc_id': [f'DOC_{i+1:02d}' for i in range(len(discharge_summaries))],
    'text': discharge_summaries
})

print(f"Loaded {len(df)} discharge summaries.")
print("\n--- Sample document (DOC_01) ---")
print(df['text'][0])
```

**Run this cell.** You should see 15 documents loaded and the first discharge summary printed.

**Look at the raw text and notice:**
- Abbreviations: `Pt`, `M`, `F`, `w/`, `Hx`, `T2DM`, `HTN`
- Drug doses: `Metformin 500mg BD`
- Noise: `/`, `x2`, `q2h`, numbers

---

## Step 3 — Basic Cleaning

Now you will clean the text. We will do this in stages so you can see what each step does.

```python
import re
import string

stop_words = set(stopwords.words('english'))

def basic_clean(text):
    """Lowercase, remove punctuation and digits, remove extra whitespace."""
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Remove digits
    text = re.sub(r'\d+', '', text)
    # Collapse multiple spaces
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Apply basic cleaning
df['cleaned'] = df['text'].apply(basic_clean)

print("--- Raw vs Cleaned (DOC_01) ---")
print("RAW:")
print(df['text'][0])
print("\nCLEANED:")
print(df['cleaned'][0])
```

**What changed?** All text is now lowercase. Punctuation and numbers are removed. Notice abbreviations like `t2dm` become `tdm` — this shows one of the trade-offs of aggressive cleaning.

---

## Step 4 — Tokenize and Remove Stopwords

```python
def tokenize_and_remove_stopwords(text):
    """Split into words and remove common English stopwords."""
    tokens = word_tokenize(text)
    # Keep only alphabetic tokens (no single chars, no noise)
    tokens = [t for t in tokens if t.isalpha() and len(t) > 1]
    # Remove stopwords
    tokens = [t for t in tokens if t not in stop_words]
    return tokens

df['tokens'] = df['cleaned'].apply(tokenize_and_remove_stopwords)

print("--- Tokens for DOC_01 ---")
print(df['tokens'][0])
print(f"\nOriginal word count: {len(df['text'][0].split())}")
print(f"Token count after cleaning: {len(df['tokens'][0])}")
```

**Expected output:** You will see a list of meaningful words. Stopwords like `the`, `is`, `and`, `for` are gone. This reduces noise significantly.

---

## Step 5 — Stemming with Porter Stemmer

Stemming cuts words to their root form using simple rules. It is fast but sometimes produces non-words.

```python
stemmer = PorterStemmer()

def stem_tokens(tokens):
    return [stemmer.stem(t) for t in tokens]

df['stemmed'] = df['tokens'].apply(stem_tokens)
df['stemmed_text'] = df['stemmed'].apply(lambda tokens: ' '.join(tokens))

# Compare a few words
example_words = ['admitted', 'admitting', 'discharge', 'discharged', 'medication', 'medications']
print("--- Stemming Examples ---")
for word in example_words:
    print(f"  {word:20s} → {stemmer.stem(word)}")

print("\n--- Stemmed tokens for DOC_01 ---")
print(df['stemmed'][0])
```

**Look at the stems.** Notice: `admitted` → `admit`, `discharged` → `discharg`, `medications` → `medic`. Stems are not real words but they group similar words together.

---

## Step 6 — Lemmatization with spaCy

Lemmatization is smarter — it uses vocabulary and grammar to find the true root word (the lemma).

```python
def lemmatize_text(text):
    """Use spaCy to lemmatize text."""
    doc = nlp(text)
    # Keep only alphabetic tokens, not stopwords, with length > 1
    lemmas = [
        token.lemma_ 
        for token in doc 
        if token.is_alpha and not token.is_stop and len(token.text) > 1
    ]
    return lemmas

# We lemmatize the cleaned text (not the stemmed version)
df['lemmatized'] = df['cleaned'].apply(lemmatize_text)
df['lemmatized_text'] = df['lemmatized'].apply(lambda tokens: ' '.join(tokens))

# Compare stemming vs lemmatization
comparison_words = ['admitted', 'discharge', 'medications', 'prescribed', 'monitoring']
print("--- Stem vs Lemma Comparison ---")
print(f"{'Word':<20} {'Stem':<20} {'Lemma':<20}")
print("-" * 60)
for word in comparison_words:
    stem = stemmer.stem(word)
    lemma = nlp(word)[0].lemma_
    print(f"{word:<20} {stem:<20} {lemma:<20}")

print("\n--- Lemmatized tokens for DOC_01 ---")
print(df['lemmatized'][0])
```

**Key difference to notice:** `medications` → stem is `medic`, lemma is `medication`. Lemmatization keeps real words.

---

## Step 7 — Extract TF-IDF Keywords

TF-IDF finds words that are frequent in a document but rare across all documents — these are the "signature" words.

```python
def get_top_keywords(tfidf_matrix, feature_names, doc_index, n=10):
    """Return the top n keywords for a given document."""
    row = tfidf_matrix[doc_index]
    # Get indices sorted by TF-IDF score descending
    sorted_indices = np.argsort(row.toarray()[0])[::-1]
    top_keywords = [(feature_names[i], round(row.toarray()[0][i], 4)) 
                    for i in sorted_indices[:n]]
    return top_keywords

# --- TF-IDF on raw text ---
vectorizer_raw = TfidfVectorizer(max_features=500)
tfidf_raw = vectorizer_raw.fit_transform(df['text'])
features_raw = vectorizer_raw.get_feature_names_out()

# --- TF-IDF on stemmed text ---
vectorizer_stem = TfidfVectorizer(max_features=500)
tfidf_stem = vectorizer_stem.fit_transform(df['stemmed_text'])
features_stem = vectorizer_stem.get_feature_names_out()

# --- TF-IDF on lemmatized text ---
vectorizer_lemma = TfidfVectorizer(max_features=500)
tfidf_lemma = vectorizer_lemma.fit_transform(df['lemmatized_text'])
features_lemma = vectorizer_lemma.get_feature_names_out()

print("TF-IDF vectorizers fitted successfully.")
print(f"Vocabulary size — Raw: {len(features_raw)}, Stemmed: {len(features_stem)}, Lemmatized: {len(features_lemma)}")
```

---

## Step 8 — Build the Keyword Comparison Table

```python
# Build comparison for the first 5 documents
results = []

for i in range(5):
    raw_kws = [kw for kw, _ in get_top_keywords(tfidf_raw, features_raw, i, n=5)]
    stem_kws = [kw for kw, _ in get_top_keywords(tfidf_stem, features_stem, i, n=5)]
    lemma_kws = [kw for kw, _ in get_top_keywords(tfidf_lemma, features_lemma, i, n=5)]
    
    results.append({
        'Doc ID': df['doc_id'][i],
        'Raw Top-5 Keywords': ', '.join(raw_kws),
        'Stemmed Top-5 Keywords': ', '.join(stem_kws),
        'Lemmatized Top-5 Keywords': ', '.join(lemma_kws),
    })

comparison_df = pd.DataFrame(results)

# Display the table
pd.set_option('display.max_colwidth', 60)
print("\n=== Keyword Comparison Table ===")
print(comparison_df.to_string(index=False))
```

**Expected output:** A table showing 3 columns of keywords for each document. Look at which version gives the most meaningful clinical terms.

---

## Step 9 — Analyze the Results

```python
# Let's do a deeper look at one document
doc_idx = 0  # DOC_01

print(f"\n=== Deep Dive: {df['doc_id'][doc_idx]} ===")
print(f"Summary: {df['text'][doc_idx][:100]}...")

print("\n--- Top 10 Keywords (Raw) ---")
for kw, score in get_top_keywords(tfidf_raw, features_raw, doc_idx, n=10):
    print(f"  {kw:<25} score: {score}")

print("\n--- Top 10 Keywords (Stemmed) ---")
for kw, score in get_top_keywords(tfidf_stem, features_stem, doc_idx, n=10):
    print(f"  {kw:<25} score: {score}")

print("\n--- Top 10 Keywords (Lemmatized) ---")
for kw, score in get_top_keywords(tfidf_lemma, features_lemma, doc_idx, n=10):
    print(f"  {kw:<25} score: {score}")
```

---

## Step 10 — Document Your Findings

At the bottom of your notebook, add a markdown cell (or a print statement) with answers to these questions:

```python
findings = """
=== MY FINDINGS ===

1. Which preprocessing method produced the most meaningful clinical keywords?
   Answer: [Write your observation here]

2. What clinical information was lost in the stemmed version?
   Example: [Give a specific word example from your output]

3. Did any junk keywords appear in the raw TF-IDF output?
   Example: [List any non-meaningful words you saw]

4. Which method would you choose for a clinical coding system and why?
   Answer: [Your reasoning]
"""
print(findings)
```

Fill in your observations based on what you actually saw in the output.

---

## Expected Output Summary

After running all steps you should have:

| What | Expected Result |
|------|----------------|
| Dataset loaded | 15 discharge summaries in a DataFrame |
| Cleaned text | Lowercase, no punctuation, no digits |
| Token count | Each doc reduced from ~50 words to ~20-30 tokens |
| Stems | Non-words like `discharg`, `medic`, `administr` |
| Lemmas | Real words like `discharge`, `medication`, `administer` |
| Comparison table | 5 rows × 3 keyword columns |

---

## Key Concepts Explained

**Tokenization:** Splitting text into individual words (tokens). `"chest pain"` → `["chest", "pain"]`.

**Stopwords:** Common words with no meaning for analysis (`the`, `is`, `was`, `of`). Removing them reduces noise.

**Stemming:** Cuts word endings using rules. Fast but imprecise. `running → run`, `studies → studi`.

**Lemmatization:** Uses a dictionary to find the base form. Slower but accurate. `running → run`, `studies → study`.

**TF-IDF:** Term Frequency × Inverse Document Frequency. High score = word appears often in THIS doc but rarely in other docs → likely a signature/key term.

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `ModuleNotFoundError: No module named 'nltk'` | Run `pip install nltk` in terminal |
| `OSError: [E050] Can't find model 'en_core_web_sm'` | Run `python -m spacy download en_core_web_sm` |
| `LookupError: punkt` | Run `nltk.download('punkt')` and `nltk.download('punkt_tab')` |
| Empty token lists | Check that `cleaned` column is not empty; re-run Step 3 |

---

## What to Submit

1. Your completed `lab1a_preprocessing.py` or `.ipynb` file with all cells executed.
2. Screenshot or copy of the **keyword comparison table** from Step 8.
3. Written answers to the 4 findings questions from Step 10.
