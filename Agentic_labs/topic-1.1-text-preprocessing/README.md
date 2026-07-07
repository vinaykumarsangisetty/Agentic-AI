# Topic 1.1: Text Preprocessing and Representations

## 🎯 Learning Objectives

By completing these exercises, you will:
- Master essential text preprocessing techniques for NLP pipelines
- Understand different tokenization strategies and their trade-offs
- Implement stemming and lemmatization with proper use cases
- Build Bag of Words and TF-IDF representations
- Work with word embeddings (Word2Vec, GloVe, FastText)
- Compare sparse vs dense text representations

## 📖 Concept Overview

### Text Preprocessing
Raw text requires cleaning before being fed into ML models. Common steps:
- **Lowercasing**: Normalize case to reduce vocabulary size
- **Punctuation removal**: Remove non-informative characters
- **Stopword removal**: Filter common words (the, is, at)
- **Noise cleaning**: Remove URLs, HTML tags, special characters

### Tokenization
Breaking text into meaningful units:
- **Character-level**: Individual characters (useful for spelling, languages without word boundaries)
- **Word-level**: Split by spaces/punctuation
- **Subword-level**: BPE, WordPiece, SentencePiece — critical for LLMs to handle unknown words

### Stemming vs Lemmatization
- **Stemming**: Fast, rule-based suffix removal (running → run, better → better)
- **Lemmatization**: Slower, dictionary-based word form reduction (running → run, better → good)

### Text Representations
- **Bag of Words (BoW)**: Word counts, ignores order and context
- **TF-IDF**: Weights words by importance (frequent in document, rare in corpus)
- **Word Embeddings**: Dense vectors capturing semantic relationships

## 🏋️ Exercise Structure

### Beginner Level
- **Demo**: Basic text preprocessing pipeline
- **Practice 1**: Tokenization comparison
- **Practice 2**: Bag of Words implementation

### Intermediate Level
- **Demo**: TF-IDF from scratch and sklearn comparison
- **Practice 1**: Stemming vs lemmatization analysis
- **Practice 2**: Word2Vec training and exploration

### Advanced Level
- **Demo**: Production preprocessing pipeline with error handling
- **Practice 1**: Subword tokenization for LLMs
- **Practice 2**: Embedding comparison (Word2Vec vs GloVe vs Azure OpenAI)

## 💻 Required Libraries

```python
import nltk
import spacy
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from gensim.models import Word2Vec, FastText
import numpy as np
```

## 📊 Datasets Used

- **Beginner**: Small sample texts (provided in code)
- **Intermediate**: Movie reviews, news articles
- **Advanced**: Large text corpus, multi-language data

## 🎓 Key Takeaways

1. **Preprocessing is context-dependent**: Social media needs different preprocessing than legal documents
2. **Subword tokenization** enables LLMs to handle rare/unknown words efficiently
3. **TF-IDF** is still valuable for keyword extraction and simple retrieval tasks
4. **Word embeddings** capture semantic similarity but require large training data or pre-trained models
5. **Trade-offs matter**: Speed vs accuracy, memory vs performance

## 🔗 Connection to Later Modules

- **Module 2-3**: Embeddings used in vector databases and RAG
- **Module 4**: Tokenization critical for prompt engineering
- **Module 6**: Preprocessing affects evaluation quality
