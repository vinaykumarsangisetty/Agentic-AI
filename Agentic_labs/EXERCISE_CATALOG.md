# NLP Labs - Exercise Catalog

Complete listing of all hands-on exercises in this repository.

---

## 📚 Topic 1.1: Text Preprocessing

**Location**: `topic-1.1-text-preprocessing/exercises/`  
**Concepts**: Tokenization, stopwords, Bag of Words

### Demo: Basic Text Preprocessing Pipeline
**Files**: `demo_exercise.py`, `demo_solution.py`  
**Learn**: Clean text (URLs, emails, punctuation), remove stopwords, build reusable pipeline  
**Time**: 30-45 minutes

### Practice 1: Tokenization Strategies
**Files**: `practice1_exercise.py`, `practice1_solution.py`  
**Learn**: Character tokenization, word tokenization, NLTK tokenizers  
**Time**: 45-60 minutes

### Practice 2: Bag of Words Implementation
**Files**: `practice2_exercise.py`, `practice2_solution.py`  
**Learn**: Build vocabulary, create BoW vectors, compare documents  
**Time**: 45-60 minutes

---

## 📚 Topic 1.2: Semantic Similarity

**Location**: `topic-1.2-semantic-similarity/exercises/`  
**Concepts**: Cosine similarity, inverted index, BM25

### Demo: Cosine Similarity from Scratch
**Files**: `demo_exercise.py`, `demo_solution.py`  
**Learn**: Dot product, magnitude calculation, sklearn comparison  
**Time**: 30-45 minutes

### Practice 1: Inverted Index Search
**Files**: `practice1_exercise.py`, `practice1_solution.py`  
**Learn**: Build inverted index, posting lists, boolean search  
**Time**: 60-75 minutes

### Practice 2: BM25 Ranking Algorithm
**Files**: `practice2_exercise.py`, `practice2_solution.py`  
**Learn**: BM25 formula, parameter tuning (k1, b), ranking results  
**Time**: 60-75 minutes

---

## 📚 Topic 1.3: NER & Classification

**Location**: `topic-1.3-ner-classification/exercises/`  
**Concepts**: Named entity recognition, sentiment analysis, evaluation metrics

### Demo: Rule-Based NER
**Files**: `demo_exercise.py`, `demo_solution.py`  
**Learn**: Regex patterns for emails, URLs, phones, dates  
**Time**: 30-45 minutes

### Practice 1: Sentiment Analysis with Naive Bayes
**Files**: `practice1_exercise.py`, `practice1_solution.py`  
**Learn**: Text classification, Naive Bayes, sklearn pipeline  
**Time**: 60-75 minutes

### Practice 2: Evaluation Metrics Deep Dive
**Files**: `practice2_exercise.py`, `practice2_solution.py`  
**Learn**: Precision, recall, F1-score, confusion matrix  
**Time**: 45-60 minutes

---

## 📚 Topic 1.4: RAG & GenAI

**Location**: `topic-1.4-rag/exercises/`  
**Concepts**: End-to-end pipelines, embeddings, Retrieval-Augmented Generation

### Demo: End-to-End NLP Pipeline
**Files**: `demo_exercise.py`, `demo_solution.py`  
**Learn**: sklearn Pipeline, feature engineering, chaining components  
**Time**: 45-60 minutes

### Practice 1: BoW vs Word Embeddings
**Files**: `practice1_exercise.py`, `practice1_solution.py`  
**Learn**: Compare representations, semantic similarity, use cases  
**Time**: 60-75 minutes

### Practice 2: Simple RAG Pipeline
**Files**: `practice2_exercise.py`, `practice2_solution.py`  
**Learn**: Document chunking, embeddings, retrieval, generation with Azure OpenAI  
**Time**: 75-90 minutes  
**Requirements**: Azure OpenAI access

---

## 📊 Summary

**Total Exercises**: 12 (4 topics × 3 exercises each)  
**Total Files**: 24 (each exercise has starter + solution)  
**Estimated Time**: 15-18 hours total  
**Prerequisites**: Python 3.8+, basic NLP understanding

---

## 🎯 Recommended Order

1. **Start with demos** to understand core concepts
2. **Complete practice exercises** to reinforce learning
3. **Compare your solutions** with provided solution files
4. **Experiment** with different parameters and datasets

---

## 💡 Tips for Success

- Read the topic README before starting exercises
- Follow TODO instructions step-by-step
- Run code frequently to test as you go
- Use VS Code debugger for complex issues
- Review solution files for best practices
- Try modifying exercises with your own data

---

## 🔧 Setup Requirements

**All Exercises**:
- Python 3.8+
- Packages from `requirements.txt`
- VS Code (recommended)

**Topic 1.4 Only**:
- Azure OpenAI account
- `.env` file configured

See [QUICK_START.md](QUICK_START.md) for setup instructions.
