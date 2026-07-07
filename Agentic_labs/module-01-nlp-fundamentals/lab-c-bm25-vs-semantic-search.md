# Lab 1C — BM25 Keyword Search vs Semantic Search

**Module:** 1 — NLP Fundamentals  
**Difficulty:** Intermediate  
**Duration:** 45 minutes  
**What you'll build:** A script that builds two search engines — one keyword-based (BM25), one meaning-based (semantic) — and compares their results on banking FAQ queries.

---

## Why This Matters

A bank's customer support portal needs to match customer questions to relevant FAQs. Customers say `"Can I skip my EMI this month?"` but the FAQ says `"Installment deferral policy"`. A keyword search fails because `EMI` ≠ `installment`. A semantic search succeeds because it understands meaning. This lab demonstrates that gap — and when each approach wins.

---

## Learning Objectives

1. Build a BM25 keyword retrieval index.
2. Build a FAISS semantic retrieval index using sentence embeddings.
3. Run the same queries through both systems.
4. Identify which system fails and why.
5. Recommend a retrieval strategy.

---

## Prerequisites

```bash
pip install rank-bm25 sentence-transformers faiss-cpu pandas numpy
```

---

## Dataset

You will use 20 banking FAQ entries embedded directly in the code below.

---

## Step 1 — Import Libraries

```python
import numpy as np
import pandas as pd
from rank_bm25 import BM25Okapi
import faiss
from sentence_transformers import SentenceTransformer
import warnings
warnings.filterwarnings('ignore')

print("Libraries imported.")
```

---

## Step 2 — Load the Banking FAQ Dataset

This is your document corpus — the knowledge base that the search engines will search through.

```python
faq_data = [
    {
        "id": "FAQ_001",
        "question": "How do I apply for a home loan?",
        "answer": "You can apply for a home loan online through our portal or visit any branch. "
                  "You will need your income proof, identity documents, and property details. "
                  "Approval typically takes 3-5 working days."
    },
    {
        "id": "FAQ_002",
        "question": "What is the interest rate on personal loans?",
        "answer": "Personal loan interest rates range from 10.5% to 18% per annum, "
                  "depending on your credit score, income, and loan tenure. "
                  "Apply online to get your personalized rate."
    },
    {
        "id": "FAQ_003",
        "question": "How can I defer my EMI payment?",
        "answer": "Installment deferral is available for customers facing financial hardship. "
                  "You may request a moratorium of up to 3 months. "
                  "Contact our customer care or log in to the app to raise a deferral request."
    },
    {
        "id": "FAQ_004",
        "question": "What documents are required to open a savings account?",
        "answer": "To open a savings account you need: a valid government-issued photo ID "
                  "(Aadhaar, Passport, or Driving License), PAN card, and proof of address "
                  "(utility bill or bank statement from the last 3 months)."
    },
    {
        "id": "FAQ_005",
        "question": "How do I report a lost or stolen debit card?",
        "answer": "If your debit card is lost or stolen, immediately call our 24x7 helpline "
                  "at 1800-XXX-XXXX or block the card through the mobile app under 'Card Services'. "
                  "A replacement card will be dispatched within 5-7 working days."
    },
    {
        "id": "FAQ_006",
        "question": "What is the minimum balance requirement for a savings account?",
        "answer": "The minimum average monthly balance (AMB) for a regular savings account is ₹10,000 "
                  "for urban branches and ₹5,000 for rural/semi-urban branches. "
                  "Non-maintenance charges apply if balance falls below the threshold."
    },
    {
        "id": "FAQ_007",
        "question": "How do I transfer money internationally?",
        "answer": "International wire transfers (SWIFT) can be initiated through net banking "
                  "under the 'Remittance' section. You will need the recipient's IBAN/account number, "
                  "bank name, SWIFT code, and country. Charges apply per transaction."
    },
    {
        "id": "FAQ_008",
        "question": "What is the maximum daily ATM withdrawal limit?",
        "answer": "The default daily ATM withdrawal limit is ₹25,000. "
                  "This can be increased up to ₹1,00,000 through net banking or by visiting a branch. "
                  "Temporary limit enhancements are also available for travel purposes."
    },
    {
        "id": "FAQ_009",
        "question": "How do I dispute a fraudulent transaction?",
        "answer": "If you notice an unauthorized or suspicious charge on your account, "
                  "log in to the app and go to 'Dispute a Transaction' under Account Services. "
                  "You can also call our fraud helpline within 24 hours of the transaction. "
                  "Provisional credit is issued within 3 business days while we investigate."
    },
    {
        "id": "FAQ_010",
        "question": "What is a fixed deposit and how do I open one?",
        "answer": "A fixed deposit (FD) is a savings instrument where you deposit a lump sum "
                  "for a fixed period at a guaranteed interest rate. "
                  "Open an FD through net banking, the mobile app, or at any branch. "
                  "Tenures range from 7 days to 10 years."
    },
    {
        "id": "FAQ_011",
        "question": "How is my credit score calculated?",
        "answer": "Your credit score (CIBIL score in India) is calculated based on payment history (35%), "
                  "credit utilization (30%), length of credit history (15%), credit mix (10%), "
                  "and new credit inquiries (10%). Paying bills on time and keeping utilization below 30% "
                  "improves your score."
    },
    {
        "id": "FAQ_012",
        "question": "Can I prepay my home loan without penalty?",
        "answer": "Yes, you can make partial or full prepayment on your home loan. "
                  "For floating-rate loans, there is no prepayment penalty as per RBI guidelines. "
                  "For fixed-rate loans, a fee of up to 2% of the prepaid amount may apply."
    },
    {
        "id": "FAQ_013",
        "question": "How do I activate my credit card?",
        "answer": "Your new credit card can be activated by calling the number printed on the card, "
                  "through the mobile banking app under 'Card Management', "
                  "or by completing the first transaction at a PoS terminal or ATM."
    },
    {
        "id": "FAQ_014",
        "question": "What happens if I miss a credit card payment?",
        "answer": "Missing a payment results in a late payment fee, interest charged on the outstanding balance "
                  "(typically 2.5-3.5% per month), and a negative impact on your credit score. "
                  "We recommend setting up auto-pay to avoid missed payments."
    },
    {
        "id": "FAQ_015",
        "question": "How do I apply for an education loan?",
        "answer": "Education loans are available for courses in India and abroad. "
                  "Eligible courses include UG, PG, diplomas, and professional programs. "
                  "You need admission proof, course details, cost of education, co-borrower income proof. "
                  "Loans up to ₹7.5 lakh require no collateral."
    },
    {
        "id": "FAQ_016",
        "question": "What is net banking and how do I register?",
        "answer": "Net banking gives you 24x7 access to your accounts online. "
                  "Register by visiting our website and clicking 'Register for Net Banking'. "
                  "You will need your account number, registered mobile number, and debit card details."
    },
    {
        "id": "FAQ_017",
        "question": "How do I update my mobile number linked to my account?",
        "answer": "To update your registered mobile number, visit any branch with valid ID proof, "
                  "or update it through our net banking portal under 'Profile Settings'. "
                  "The new number is linked within 24 hours."
    },
    {
        "id": "FAQ_018",
        "question": "Is my bank account DICGC insured?",
        "answer": "Yes, deposits with our bank are insured under the DICGC (Deposit Insurance and Credit "
                  "Guarantee Corporation) scheme up to ₹5 lakh per depositor per bank, "
                  "covering both principal and interest."
    },
    {
        "id": "FAQ_019",
        "question": "How do I check if my cheque has been cleared?",
        "answer": "You can check cheque clearing status through net banking under 'Account Statement', "
                  "the mobile app, or by calling our helpline. "
                  "Cheques deposited before 2 PM are typically processed the same day."
    },
    {
        "id": "FAQ_020",
        "question": "What is the difference between NEFT, RTGS, and IMPS?",
        "answer": "NEFT (National Electronic Funds Transfer) is processed in hourly batches, free for online transfers. "
                  "RTGS (Real Time Gross Settlement) is for high-value transfers (min ₹2 lakh), settled instantly. "
                  "IMPS (Immediate Payment Service) works 24x7 including holidays, instant transfers up to ₹5 lakh."
    },
]

df_faq = pd.DataFrame(faq_data)

# The 'document' field combines question + answer for richer context
df_faq['document'] = df_faq['question'] + " " + df_faq['answer']

print(f"Loaded {len(df_faq)} FAQ documents.")
print("\n--- Sample FAQ (FAQ_003) ---")
print(f"Q: {df_faq.loc[2, 'question']}")
print(f"A: {df_faq.loc[2, 'answer'][:150]}...")
```

---

## Step 3 — Build the BM25 Index

BM25 is the gold standard for keyword search. It ranks documents by how often query terms appear, adjusted for document length.

```python
# Tokenize documents for BM25 (simple whitespace split + lowercase)
def tokenize_for_bm25(text):
    return text.lower().split()

tokenized_corpus = [tokenize_for_bm25(doc) for doc in df_faq['document']]

# Build BM25 index
bm25 = BM25Okapi(tokenized_corpus)

print("BM25 index built successfully.")
print(f"Corpus size: {len(tokenized_corpus)} documents")
print(f"Sample tokenized doc (FAQ_003 first 20 tokens):")
print(tokenized_corpus[2][:20])
```

---

## Step 4 — Build the Semantic (FAISS) Index

```python
# Load the sentence transformer model
print("\nLoading embedding model (may take a moment on first run)...")
embed_model = SentenceTransformer('all-MiniLM-L6-v2')
print("Model ready.")

# Generate embeddings for all FAQ documents
print("Generating embeddings for all documents...")
doc_embeddings = embed_model.encode(df_faq['document'].tolist(), show_progress_bar=True)

# Normalize embeddings (required for cosine similarity in FAISS)
norms = np.linalg.norm(doc_embeddings, axis=1, keepdims=True)
doc_embeddings_normalized = doc_embeddings / norms

# Build FAISS flat index (brute-force, exact search, good for small corpora)
embedding_dim = doc_embeddings_normalized.shape[1]
faiss_index = faiss.IndexFlatIP(embedding_dim)  # IP = Inner Product (cosine sim after normalization)
faiss_index.add(doc_embeddings_normalized.astype('float32'))

print(f"\nFAISS index built.")
print(f"Embedding dimension: {embedding_dim}")
print(f"Total indexed vectors: {faiss_index.ntotal}")
```

---

## Step 5 — Define Search Functions

```python
def bm25_search(query, top_k=5):
    """Search using BM25 keyword matching."""
    query_tokens = tokenize_for_bm25(query)
    scores = bm25.get_scores(query_tokens)
    
    # Get top-k document indices
    top_indices = np.argsort(scores)[::-1][:top_k]
    
    results = []
    for idx in top_indices:
        results.append({
            'rank': len(results) + 1,
            'doc_id': df_faq.loc[idx, 'id'],
            'question': df_faq.loc[idx, 'question'],
            'bm25_score': round(float(scores[idx]), 4)
        })
    return results


def semantic_search(query, top_k=5):
    """Search using semantic embeddings and FAISS."""
    # Encode and normalize the query
    query_vec = embed_model.encode([query])
    query_vec_norm = query_vec / np.linalg.norm(query_vec, axis=1, keepdims=True)
    
    # Search FAISS index
    scores, indices = faiss_index.search(query_vec_norm.astype('float32'), top_k)
    
    results = []
    for rank, (score, idx) in enumerate(zip(scores[0], indices[0])):
        results.append({
            'rank': rank + 1,
            'doc_id': df_faq.loc[idx, 'id'],
            'question': df_faq.loc[idx, 'question'],
            'semantic_score': round(float(score), 4)
        })
    return results


def compare_search(query, top_k=5):
    """Run both search methods and display results side-by-side."""
    bm25_results = bm25_search(query, top_k)
    sem_results = semantic_search(query, top_k)
    
    print(f"\n{'='*80}")
    print(f"QUERY: \"{query}\"")
    print(f"{'='*80}")
    print(f"\n{'Rank':<6} {'BM25 Result':<45} {'Semantic Result':<45}")
    print(f"{'-'*6} {'-'*45} {'-'*45}")
    
    for i in range(top_k):
        bm25_q = bm25_results[i]['question'][:42] + "..." if len(bm25_results[i]['question']) > 42 else bm25_results[i]['question']
        sem_q = sem_results[i]['question'][:42] + "..." if len(sem_results[i]['question']) > 42 else sem_results[i]['question']
        print(f"{i+1:<6} {bm25_q:<45} {sem_q:<45}")
    
    return bm25_results, sem_results

print("Search functions defined.")
```

---

## Step 6 — Run Your Test Queries

Now test both systems with 8 different queries. Pay close attention to when they agree and when they disagree.

```python
# Test queries — some use exact FAQ vocabulary, some use different phrasing
test_queries = [
    # --- Exact vocabulary match (BM25 should win) ---
    ("Q1 — Exact Match", "How do I apply for a home loan?"),
    
    # --- Paraphrase / vocabulary mismatch (Semantic should win) ---
    ("Q2 — Paraphrase", "Can I skip my monthly installment?"),      # FAQ says "defer EMI"
    ("Q3 — Synonym", "My debit card was stolen, what do I do?"),     # FAQ says "lost or stolen"
    ("Q4 — Conceptual", "I want to save money for a fixed period"),  # FAQ is about FDs
    
    # --- Partial vocabulary overlap ---
    ("Q5 — Partial Match", "transfer money to another country"),     # FAQ says "internationally"
    ("Q6 — Abbreviation", "What is IMPS and how is it different?"),  # Tests acronym handling
    
    # --- Multi-concept query ---
    ("Q7 — Multi-concept", "unauthorized charge on my account"),     # Related to fraud FAQ
    ("Q8 — Low vocab overlap", "my CIBIL score is bad, how to fix it?"),  # FAQ talks about credit score
]

all_results = {}

for label, query in test_queries:
    bm25_res, sem_res = compare_search(query, top_k=3)
    all_results[label] = {
        'query': query,
        'bm25_top1': bm25_res[0]['question'],
        'semantic_top1': sem_res[0]['question'],
        'bm25_score': bm25_res[0]['bm25_score'],
        'semantic_score': sem_res[0]['semantic_score'],
    }
```

---

## Step 7 — Build a Relevance-Labeled Comparison Table

Now manually label whether the top result from each system is relevant.

```python
# Ground truth — manually label which FAQ is the correct answer for each query
ground_truth = {
    "Q1 — Exact Match":    "FAQ_001",  # home loan
    "Q2 — Paraphrase":     "FAQ_003",  # defer EMI = skip installment
    "Q3 — Synonym":        "FAQ_005",  # lost/stolen debit card
    "Q4 — Conceptual":     "FAQ_010",  # fixed deposit
    "Q5 — Partial Match":  "FAQ_007",  # international transfer
    "Q6 — Abbreviation":   "FAQ_020",  # NEFT/RTGS/IMPS
    "Q7 — Multi-concept":  "FAQ_009",  # dispute fraudulent transaction
    "Q8 — Low vocab overlap": "FAQ_011",  # credit score
}

# Evaluate precision@1 for each method
bm25_correct = 0
semantic_correct = 0

report_rows = []

for label, query in test_queries:
    bm25_res = bm25_search(query, top_k=5)
    sem_res = semantic_search(query, top_k=5)
    
    correct_id = ground_truth[label]
    bm25_top1_id = bm25_res[0]['doc_id']
    sem_top1_id = sem_res[0]['doc_id']
    
    bm25_hit = "✓" if bm25_top1_id == correct_id else "✗"
    sem_hit = "✓" if sem_top1_id == correct_id else "✗"
    
    if bm25_top1_id == correct_id:
        bm25_correct += 1
    if sem_top1_id == correct_id:
        semantic_correct += 1
    
    report_rows.append({
        'Query Label': label,
        'Query': query[:50] + "..." if len(query) > 50 else query,
        'Correct FAQ': correct_id,
        'BM25 Top-1': bm25_top1_id,
        'BM25 Correct?': bm25_hit,
        'Semantic Top-1': sem_top1_id,
        'Semantic Correct?': sem_hit,
    })

report_df = pd.DataFrame(report_rows)

print("\n=== RETRIEVAL ACCURACY REPORT ===")
print(report_df.to_string(index=False))

print(f"\n--- Precision@1 Summary ---")
print(f"BM25 Precision@1:     {bm25_correct}/{len(test_queries)} = {bm25_correct/len(test_queries)*100:.1f}%")
print(f"Semantic Precision@1: {semantic_correct}/{len(test_queries)} = {semantic_correct/len(test_queries)*100:.1f}%")
```

**Expected result:** Semantic search should outperform BM25 on paraphrase and synonym queries. BM25 may match well on exact-vocabulary queries.

---

## Step 8 — Failure Analysis

```python
print("\n=== FAILURE ANALYSIS ===")

print("\n--- BM25 Failure Cases ---")
print("BM25 fails when the customer uses DIFFERENT words than the FAQ.")
print("Example failures:")
print("  'skip monthly installment' vs 'defer EMI' — BM25 cannot match these")
print("  'CIBIL score' vs 'credit score' — BM25 misses the synonym")
print("  'I want to save money for a fixed period' — no keywords match 'fixed deposit'")

print("\n--- Semantic Search Failure Cases ---")
print("Semantic search can fail when:")
print("  1. The query contains domain-specific acronyms (IMPS, NEFT) the model does not know well")
print("  2. The corpus is very large and semantic similarity becomes noisy")
print("  3. Two documents are topically similar but contextually different")

print("\n--- Your Observations ---")
print("Look at the ✗ marks in your report. For each BM25 failure:")
print("  - What exact words in the query were NOT in the FAQ?")
print("  - Would a customer realistically write the query your way?")
print("\nFor each Semantic failure:")
print("  - What made the top result semantically close but actually wrong?")
```

---

## Step 9 — Write Your Recommendation

```python
recommendation = """
=== SEARCH STRATEGY RECOMMENDATION ===

Based on the test results, complete this recommendation:

SCENARIO: Banking customer support portal

1. BM25-only is suitable when:
   → Customers always use exact product names (e.g., "RTGS", "fixed deposit")
   → Speed and infrastructure simplicity matter more than accuracy
   → [Add your observation from the results]

2. Semantic-only is suitable when:
   → Customers describe problems in natural language ("my card doesn't work")
   → Vocabulary varies widely across customers
   → [Add your observation from the results]

3. Hybrid approach (BM25 + Semantic with score fusion) is recommended when:
   → You want best of both worlds
   → You can afford slightly higher latency
   → [Add your reasoning]

MY RECOMMENDATION FOR THIS BANKING PORTAL:
[Write your recommendation in 2-3 sentences]
"""
print(recommendation)
```

---

## Expected Output Summary

| What | Expected Result |
|------|----------------|
| BM25 Precision@1 | 50–75% (good on exact-match queries, poor on paraphrases) |
| Semantic Precision@1 | 62–100% (better on synonym and conceptual queries) |
| Comparison table | 8 rows showing top-1 result and correctness for each method |
| Report | Clear identification of failure cases for each method |

---

## Key Concepts Explained

**BM25:** A probabilistic keyword search algorithm. Ranks documents by term frequency and inverse document frequency, normalized for document length. Fast, interpretable, but cannot handle synonyms.

**Semantic Search:** Uses sentence embeddings to match by meaning. `"skip EMI"` and `"defer installment"` become similar vectors even though they share no words.

**FAISS:** Facebook AI Similarity Search — a library for fast approximate (or exact) nearest-neighbor search over high-dimensional vectors.

**Precision@1:** Did the #1 retrieved document answer the question? (1 = yes, 0 = no).

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `ModuleNotFoundError: rank_bm25` | `pip install rank-bm25` |
| `ModuleNotFoundError: faiss` | `pip install faiss-cpu` |
| All BM25 scores are 0.0 | Check that documents are not empty; re-run Step 2 |
| FAISS search returns wrong results | Verify normalization in Step 4; ensure `float32` cast |

---

## What to Submit

1. Your completed `lab1c_bm25_semantic.py` or `.ipynb` with all cells run.
2. The printed retrieval accuracy report from Step 7.
3. Written failure analysis and recommendation from Steps 8–9.
