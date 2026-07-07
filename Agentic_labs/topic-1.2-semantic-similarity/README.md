# Topic 1.2: Semantic Similarity and Information Retrieval

## 🎯 Learning Objectives

By completing these exercises, you will:
- Master semantic similarity vs lexical similarity
- Understand and implement distance metrics (Cosine, Euclidean, Manhattan)
- Build inverted indexes for efficient retrieval
- Implement BM25 ranking algorithm
- Combine keyword and vector search (hybrid search)
- Integrate with Azure AI Search

## 📖 Concept Overview

### Cosine Similarity
Measures angle between vectors, ignoring magnitude:
```
cosine_sim(A, B) = (A · B) / (||A|| × ||B||)
```
Range: [-1, 1], where 1 = identical direction, 0 = orthogonal, -1 = opposite

### Lexical vs Semantic Similarity
- **Lexical**: Based on word overlap (Jaccard, edit distance)
- **Semantic**: Based on meaning (embedding similarity)
- Example: "car" and "automobile" have low lexical but high semantic similarity

### Distance Metrics
- **Euclidean**: Straight-line distance, sensitive to magnitude
- **Manhattan**: Sum of absolute differences, less sensitive to outliers
- **Cosine**: Angle-based, normalized for magnitude

### Inverted Index
```
Term → [Doc1, Doc2, ...]
"cat" → [doc1, doc5, doc12]
"dog" → [doc1, doc3, doc15]
```
Enables efficient keyword search in O(k) where k = matching documents

### BM25
Probabilistic ranking function:
```
BM25(q, d) = Σ IDF(qi) × (f(qi,d) × (k1 + 1)) / (f(qi,d) + k1 × (1 - b + b × |d|/avgdl))
```
- k1: Term frequency saturation (typical: 1.2-2.0)
- b: Document length normalization (typical: 0.75)

## 🏋️ Exercise Structure

### Beginner Level
- **Demo**: Cosine similarity from scratch
- **Practice 1**: Building an inverted index
- **Practice 2**: BM25 implementation

### Intermediate Level
- **Demo**: Semantic vs lexical similarity
- **Practice 1**: Distance metrics comparison
- **Practice 2**: Hybrid search implementation

### Advanced Level
- **Demo**: Scalable search with FAISS
- **Practice 1**: Re-ranking pipeline
- **Practice 2**: Azure AI Search integration

## 💻 Required Libraries

```python
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from rank_bm25 import BM25Okapi
import faiss  # For advanced exercises
from openai import AzureOpenAI  # For embeddings
```

## 📊 Datasets

- **Beginner**: Small document collections (provided)
- **Intermediate**: Product descriptions, news articles
- **Advanced**: Large document corpus, Azure integration

## 🎓 Key Takeaways

1. **Cosine similarity** is standard for text (normalized, handles different document lengths)
2. **Semantic similarity** critical for RAG - captures meaning, not just word overlap
3. **BM25** still excellent for keyword search (faster than embeddings)
4. **Hybrid search** combines best of both worlds (keyword + semantic)
5. **Vector databases** essential for production semantic search at scale

## 🔗 Connection to Later Modules

- **Module 2-3**: Vector databases for RAG
- **Module 4**: Retrieval in RAG pipelines
- **Module 6**: Evaluating retrieval quality (precision@k, recall@k, MRR)
