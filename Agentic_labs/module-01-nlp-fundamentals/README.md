# Module 1 — NLP Fundamentals

**Day:** 1 | **Total Duration:** ~45 minutes | **Pick:** 1 lab to complete

## What This Module Covers

Natural Language Processing (NLP) is the foundation of every AI system that reads or generates text. Before you can build chatbots, summarizers, or search engines, you need to understand how raw text is cleaned, represented, and searched.

In this module you will work with healthcare and banking text — two high-stakes domains where text quality directly affects business outcomes.

## Lab Options

| Lab | Title | Difficulty | Duration |
|-----|-------|------------|----------|
| [Lab A](./lab-a-text-preprocessing.md) | Text Preprocessing Pipeline | Beginner | 45 min |
| [Lab B](./lab-b-word-embeddings.md) | Word Embeddings Exploration & Visualization | Beginner–Intermediate | 45 min |
| [Lab C](./lab-c-bm25-vs-semantic-search.md) | BM25 Keyword Search vs Semantic Search | Intermediate | 45 min |
| [Lab D](./lab-d-ner-enterprise-documents.md) | Named Entity Recognition on Enterprise Documents | Intermediate | 45 min |

## Recommended Starting Point

If you are new to NLP → start with **Lab A**.  
If you have done basic NLP before → try **Lab B** or **Lab C**.

## Environment Setup (Do This First)

Open a terminal and run these commands:

```bash
# Step 1 — Create a virtual environment
python -m venv nlp-env

# Step 2 — Activate it
# On Windows:
nlp-env\Scripts\activate
# On Mac/Linux:
source nlp-env/bin/activate

# Step 3 — Install all required packages
pip install pandas numpy nltk spacy scikit-learn matplotlib gensim rank-bm25 sentence-transformers faiss-cpu

# Step 4 — Download spaCy English language model
python -m spacy download en_core_web_sm
```

If `pip install` is slow, you can install packages one module at a time as needed.
