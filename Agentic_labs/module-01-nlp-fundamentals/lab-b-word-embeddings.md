# Lab 1B — Word Embeddings Exploration and Visualization

**Module:** 1 — NLP Fundamentals  
**Difficulty:** Beginner–Intermediate  
**Duration:** 45 minutes  
**What you'll build:** A script that loads a pre-trained embedding model, computes word similarities, and visualizes healthcare and banking vocabulary clusters using PCA and t-SNE.

---

## Why This Matters

Word embeddings convert words into vectors of numbers. Words with similar meanings get similar vectors. This is the foundation of semantic search, recommendation systems, and LLMs. Understanding embedding geometry helps you debug retrieval problems like "why does the system think 'loan' and 'credit' are unrelated?"

---

## Learning Objectives

1. Load a pre-trained sentence-transformers model.
2. Compute cosine similarity between word pairs.
3. Find nearest neighbors for seed words.
4. Reduce embedding dimensions using PCA and t-SNE.
5. Visualize word clusters and explain what you see.

---

## Prerequisites

Activate your virtual environment and verify:

```bash
pip install sentence-transformers scikit-learn matplotlib pandas numpy
```

---

## Setup: Create Your File

Create a new file named `lab1b_embeddings.py` (or a Jupyter notebook `lab1b_embeddings.ipynb`).

---

## Step 1 — Import Libraries and Load the Embedding Model

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sentence_transformers import SentenceTransformer

# Load a lightweight but high-quality embedding model
# This downloads ~90MB on first run — be patient
print("Loading embedding model... (this takes 1-2 minutes on first run)")
model = SentenceTransformer('all-MiniLM-L6-v2')
print("Model loaded successfully!")
print(f"Embedding dimension: {model.get_sentence_embedding_dimension()}")
```

**First run note:** The model downloads from the internet (~90MB). After the first run it is cached locally and loads in seconds.

---

## Step 2 — Compute Similarity for Word Pairs

We will test similarity on pairs from healthcare and banking vocabulary.

```python
word_pairs = [
    # Healthcare pairs
    ("diagnosis", "prognosis"),
    ("medication", "drug"),
    ("hospital", "clinic"),
    ("symptom", "sign"),
    ("surgery", "operation"),
    ("discharge", "release"),
    
    # Banking pairs
    ("loan", "credit"),
    ("interest", "rate"),
    ("mortgage", "home loan"),
    ("fraud", "scam"),
    ("deposit", "savings"),
    
    # Cross-domain (should have lower similarity)
    ("diagnosis", "loan"),
    ("surgery", "interest rate"),
    ("medication", "mortgage"),
]

print("\n=== Cosine Similarity Scores ===")
print(f"{'Word A':<20} {'Word B':<20} {'Similarity':>10}")
print("-" * 55)

similarity_results = []

for word_a, word_b in word_pairs:
    # Encode each word as a vector
    vec_a = model.encode([word_a])
    vec_b = model.encode([word_b])
    
    # Compute cosine similarity (ranges from -1 to 1, higher = more similar)
    sim = cosine_similarity(vec_a, vec_b)[0][0]
    
    similarity_results.append({
        'Word A': word_a,
        'Word B': word_b,
        'Similarity': round(float(sim), 4)
    })
    print(f"{word_a:<20} {word_b:<20} {sim:>10.4f}")

sim_df = pd.DataFrame(similarity_results)
```

**What to look for:**
- Healthcare pairs should score 0.5–0.9 (semantically related words in same domain)
- Cross-domain pairs should score 0.1–0.4 (different domains, less related)
- Near-synonyms like `surgery` / `operation` should score > 0.8

---

## Step 3 — Find Nearest Neighbors

Pick a seed word and find the 10 most similar words from a vocabulary list.

```python
# Our vocabulary — words from both domains
vocabulary = [
    # Healthcare
    "patient", "doctor", "nurse", "hospital", "clinic", "pharmacy",
    "diagnosis", "prognosis", "treatment", "therapy", "surgery", "operation",
    "medication", "drug", "prescription", "dose", "symptom", "sign",
    "discharge", "admission", "emergency", "critical", "chronic", "acute",
    "blood", "heart", "lung", "kidney", "liver", "brain",
    "cancer", "diabetes", "hypertension", "infection", "fever", "pain",
    
    # Banking
    "loan", "credit", "mortgage", "interest", "rate", "deposit",
    "savings", "account", "bank", "transaction", "payment", "transfer",
    "fraud", "risk", "compliance", "audit", "insurance", "investment",
    "bond", "stock", "portfolio", "asset", "liability", "balance",
    "branch", "teller", "ATM", "card", "PIN", "statement",
]

# Encode all vocabulary words at once (batch processing is efficient)
print("Encoding vocabulary... ")
vocab_embeddings = model.encode(vocabulary, show_progress_bar=True)
vocab_df = pd.DataFrame(vocab_embeddings, index=vocabulary)

print(f"\nVocabulary encoded: {len(vocabulary)} words")
print(f"Each word is a vector of {vocab_embeddings.shape[1]} numbers")
```

```python
def find_nearest_neighbors(seed_word, vocab_df, model, top_n=10):
    """Find the top N most similar words in the vocabulary."""
    seed_vec = model.encode([seed_word])
    
    # Compute similarity to all vocabulary words
    similarities = cosine_similarity(seed_vec, vocab_df.values)[0]
    
    # Sort by similarity descending
    sorted_indices = np.argsort(similarities)[::-1]
    
    results = []
    for idx in sorted_indices[:top_n + 1]:  # +1 in case word is in vocabulary
        word = vocab_df.index[idx]
        if word != seed_word:  # Skip the seed word itself
            results.append((word, round(float(similarities[idx]), 4)))
        if len(results) == top_n:
            break
    return results

# Test with seed words
seed_words = [
    "diagnosis",    # Healthcare clinical term
    "loan",         # Banking term
    "emergency",    # Healthcare context
    "fraud",        # Banking context
    "pain",         # Could be in either domain
]

for seed in seed_words:
    neighbors = find_nearest_neighbors(seed, vocab_df, model)
    print(f"\n--- Top 10 neighbors of '{seed}' ---")
    for i, (word, score) in enumerate(neighbors, 1):
        print(f"  {i:2}. {word:<20} similarity: {score}")
```

**Discussion:** After running, look at the neighbors for `"pain"`. Does the model cluster it with healthcare terms or banking terms? The embedding captures general language meaning, not domain-specific meaning. In Step 5, we discuss what this means for enterprise AI systems.

---

## Step 4 — Build Word List for Visualization

Select seeds and their neighbors to create a rich word list for plotting.

```python
# Select 8 seed words — 4 healthcare, 4 banking
healthcare_seeds = ["diagnosis", "surgery", "medication", "patient"]
banking_seeds = ["loan", "fraud", "mortgage", "investment"]

all_seeds = healthcare_seeds + banking_seeds

# Collect seeds + neighbors
words_to_plot = list(all_seeds)  # start with seeds
labels = {}  # word → domain label

for seed in healthcare_seeds:
    labels[seed] = 'Healthcare (seed)'
    for neighbor, _ in find_nearest_neighbors(seed, vocab_df, model, top_n=5):
        if neighbor not in words_to_plot:
            words_to_plot.append(neighbor)
            labels[neighbor] = 'Healthcare (neighbor)'

for seed in banking_seeds:
    labels[seed] = 'Banking (seed)'
    for neighbor, _ in find_nearest_neighbors(seed, vocab_df, model, top_n=5):
        if neighbor not in words_to_plot:
            words_to_plot.append(neighbor)
            labels[neighbor] = 'Banking (neighbor)'

# Fill in any words not yet labeled
for w in words_to_plot:
    if w not in labels:
        labels[w] = 'Other'

print(f"Total words selected for visualization: {len(words_to_plot)}")
print("Words:", words_to_plot)

# Get embeddings for visualization
print("\nEncoding words for visualization...")
plot_embeddings = model.encode(words_to_plot)
```

---

## Step 5 — PCA Visualization

PCA reduces the 384-dimensional embeddings to 2D while preserving the most variance.

```python
# Run PCA
pca = PCA(n_components=2, random_state=42)
embeddings_2d_pca = pca.fit_transform(plot_embeddings)

explained = pca.explained_variance_ratio_
print(f"PCA: Component 1 explains {explained[0]*100:.1f}% variance")
print(f"PCA: Component 2 explains {explained[1]*100:.1f}% variance")
print(f"Total variance explained: {sum(explained)*100:.1f}%")

# Define colors for each category
color_map = {
    'Healthcare (seed)': '#e74c3c',      # red
    'Healthcare (neighbor)': '#f1948a',  # light red
    'Banking (seed)': '#2980b9',         # blue
    'Banking (neighbor)': '#85c1e9',     # light blue
    'Other': '#95a5a6',                  # grey
}

# Plot
fig, ax = plt.subplots(figsize=(14, 10))

plotted = set()
for i, word in enumerate(words_to_plot):
    x, y = embeddings_2d_pca[i]
    category = labels.get(word, 'Other')
    color = color_map[category]
    
    # Plot dot
    label_for_legend = category if category not in plotted else None
    ax.scatter(x, y, color=color, s=100, alpha=0.8, label=label_for_legend, zorder=5)
    plotted.add(category)
    
    # Add word label (offset slightly so it doesn't overlap the dot)
    ax.annotate(word, (x, y), 
                textcoords="offset points", 
                xytext=(5, 5),
                fontsize=9,
                alpha=0.9)

ax.set_title("PCA: Word Embeddings — Healthcare vs Banking Vocabulary\n"
             f"(explains {sum(explained)*100:.1f}% of variance)", 
             fontsize=14, fontweight='bold')
ax.set_xlabel(f"PCA Component 1 ({explained[0]*100:.1f}%)")
ax.set_ylabel(f"PCA Component 2 ({explained[1]*100:.1f}%)")
ax.legend(loc='upper right', fontsize=9)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('pca_embeddings.png', dpi=150, bbox_inches='tight')
plt.show()
print("Plot saved as pca_embeddings.png")
```

**What to look for in the PCA plot:**
- Red dots (healthcare) should cluster together.
- Blue dots (banking) should cluster together.
- Are the clusters well-separated? Partially overlapping? Why?

---

## Step 6 — t-SNE Visualization

t-SNE is better at showing local cluster structure, but it does not preserve global distances.

```python
# Run t-SNE
# Note: perplexity must be less than number of samples
perplexity = min(15, len(words_to_plot) - 1)

tsne = TSNE(n_components=2, 
            perplexity=perplexity, 
            random_state=42, 
            n_iter=1000,
            learning_rate='auto',
            init='pca')

embeddings_2d_tsne = tsne.fit_transform(plot_embeddings)
print(f"t-SNE complete. Used perplexity={perplexity}")

# Plot t-SNE
fig, ax = plt.subplots(figsize=(14, 10))

plotted = set()
for i, word in enumerate(words_to_plot):
    x, y = embeddings_2d_tsne[i]
    category = labels.get(word, 'Other')
    color = color_map[category]
    
    label_for_legend = category if category not in plotted else None
    ax.scatter(x, y, color=color, s=100, alpha=0.8, label=label_for_legend, zorder=5)
    plotted.add(category)
    
    ax.annotate(word, (x, y),
                textcoords="offset points",
                xytext=(5, 5),
                fontsize=9,
                alpha=0.9)

ax.set_title("t-SNE: Word Embeddings — Healthcare vs Banking Vocabulary\n"
             f"(perplexity={perplexity})", 
             fontsize=14, fontweight='bold')
ax.set_xlabel("t-SNE Dimension 1")
ax.set_ylabel("t-SNE Dimension 2")
ax.legend(loc='upper right', fontsize=9)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('tsne_embeddings.png', dpi=150, bbox_inches='tight')
plt.show()
print("Plot saved as tsne_embeddings.png")
```

**t-SNE notes:**
- Axes have no meaning — only relative distances matter.
- Clusters are more "tight" than PCA.
- Run it twice — you may get different layouts (it's stochastic).

---

## Step 7 — Compare PCA and t-SNE

```python
# Side-by-side comparison
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 9))

for ax, embeddings_2d, title in [
    (ax1, embeddings_2d_pca, f"PCA ({sum(pca.explained_variance_ratio_)*100:.1f}% variance)"),
    (ax2, embeddings_2d_tsne, f"t-SNE (perplexity={perplexity})")
]:
    plotted = set()
    for i, word in enumerate(words_to_plot):
        x, y = embeddings_2d[i]
        category = labels.get(word, 'Other')
        color = color_map[category]
        
        label_for_legend = category if category not in plotted else None
        ax.scatter(x, y, color=color, s=80, alpha=0.8, label=label_for_legend, zorder=5)
        plotted.add(category)
        ax.annotate(word, (x, y), textcoords="offset points", 
                    xytext=(4, 4), fontsize=8, alpha=0.85)
    
    ax.set_title(title, fontsize=13, fontweight='bold')
    ax.legend(loc='upper right', fontsize=8)
    ax.grid(True, alpha=0.3)

plt.suptitle("PCA vs t-SNE: Word Embedding Visualization", fontsize=15, fontweight='bold')
plt.tight_layout()
plt.savefig('pca_vs_tsne_comparison.png', dpi=150, bbox_inches='tight')
plt.show()
print("Comparison plot saved as pca_vs_tsne_comparison.png")
```

---

## Step 8 — Document Your Observations

```python
print("""
=== OBSERVATION WORKSHEET ===

Fill in based on what you saw in your plots:

1. PCA Cluster Quality:
   - Were healthcare words well-clustered together? (Yes / Partially / No)
   - Were banking words well-clustered together? (Yes / Partially / No)
   - Which word appeared in the "wrong" cluster?

2. t-SNE Cluster Quality:
   - Did t-SNE show tighter clusters than PCA? (Yes / No / Similar)
   - Did any words appear far from their expected group? Which ones?

3. Similarity Surprises:
   - Which word pair had a HIGHER similarity than you expected?
   - Which word pair had a LOWER similarity than you expected?

4. Cross-Domain Overlap:
   - Were there words that appeared between the two clusters?
   - Why might those words be ambiguous?

5. Enterprise Application Insight:
   - If you used these embeddings for a banking chatbot semantic search,
     which healthcare words might accidentally match banking queries?
   - What does this tell you about domain-specific embeddings?
""")
```

---

## Expected Output Summary

| What | Expected Result |
|------|----------------|
| Model loaded | `all-MiniLM-L6-v2` with 384 dimensions |
| Similarity scores | `medication/drug` > 0.7, `diagnosis/loan` < 0.3 |
| Nearest neighbors | Healthcare seeds → clinical neighbors; Banking seeds → financial neighbors |
| PCA plot | Two loose clusters (some overlap) |
| t-SNE plot | Two tighter clusters, better local structure |

---

## Key Concepts Explained

**Word Embedding:** A vector (list of numbers) representing a word's meaning. Words with similar meaning have similar vectors.

**Cosine Similarity:** Measures the angle between two vectors. Value of 1 = identical direction (same meaning), 0 = perpendicular (unrelated), -1 = opposite.

**PCA (Principal Component Analysis):** Finds the 2 directions of maximum variance in the data. Good for showing global structure. Axes have meaning (variance explained %).

**t-SNE (t-distributed Stochastic Neighbor Embedding):** Focuses on preserving local neighborhood structure. Axes are meaningless. Better for showing clusters. Random seed affects output.

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `ConnectionError` when loading model | Check internet connection; the model downloads on first use |
| `ValueError: perplexity must be less than n_samples` | Reduce the word list or lower `perplexity` |
| Blank plot / no plot shown | Add `plt.ion()` at the top, or save to file and open manually |
| Very slow t-SNE | Reduce `n_iter` to 500 or reduce word list size |
| All words in one cluster | Normal for small word lists; add more words from each domain |

---

## What to Submit

1. Your completed `lab1b_embeddings.py` or `.ipynb` file.
2. Screenshots of both plots: `pca_embeddings.png` and `tsne_embeddings.png`.
3. Completed observation worksheet (Step 8).
