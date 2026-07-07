"""
===============================================================================
✅ COMPLETE SOLUTION
TOPIC 1.2 - BEGINNER DEMO: Cosine Similarity from Scratch
===============================================================================

This file contains the full working implementation.
Try the exercise file first!
"""

import numpy as np
from collections import Counter
from typing import List, Dict
from sklearn.metrics.pairwise import cosine_similarity as sklearn_cosine

# Sample documents
sample_docs = [
    "the cat sat on the mat",
    "the dog sat on the log",
    "cats and dogs are animals",
    "the quick brown fox jumps over the lazy dog"
]


def cosine_similarity(vec1: np.ndarray, vec2: np.ndarray) -> float:
    """Calculate cosine similarity between two vectors"""
    # Formula: cos(θ) = (v1 · v2) / (||v1|| * ||v2||)
    dot_product = np.dot(vec1, vec2)
    magnitude1 = np.linalg.norm(vec1)
    magnitude2 = np.linalg.norm(vec2)
    
    # Handle zero vectors
    if magnitude1 == 0 or magnitude2 == 0:
        return 0.0
    
    return dot_product / (magnitude1 * magnitude2)


def build_vocabulary(documents: List[str]) -> Dict[str, int]:
    """Build vocabulary from documents"""
    words = set()
    for doc in documents:
        words.update(doc.lower().split())
    
    sorted_words = sorted(words)
    vocabulary = {word: idx for idx, word in enumerate(sorted_words)}
    return vocabulary


def text_to_bow_vector(text: str, vocabulary: Dict[str, int]) -> np.ndarray:
    """Convert text to BoW vector"""
    vector = np.zeros(len(vocabulary))
    word_counts = Counter(text.lower().split())
    
    for word, count in word_counts.items():
        if word in vocabulary:
            vector[vocabulary[word]] = count
    
    return vector


def calculate_similarity_matrix(documents: List[str]) -> np.ndarray:
    """Calculate pairwise similarity matrix"""
    vocab = build_vocabulary(documents)
    vectors = [text_to_bow_vector(doc, vocab) for doc in documents]
    
    n = len(documents)
    sim_matrix = np.zeros((n, n))
    
    for i in range(n):
        for j in range(n):
            sim_matrix[i, j] = cosine_similarity(vectors[i], vectors[j])
    
    return sim_matrix


def compare_with_sklearn(documents: List[str]):
    """Compare our implementation with sklearn"""
    print("\n" + "="*80)
    print("COMPARING WITH SKLEARN")
    print("="*80)
    
    # Our implementation
    our_matrix = calculate_similarity_matrix(documents)
    
    # sklearn implementation
    vocab = build_vocabulary(documents)
    vectors = np.array([text_to_bow_vector(doc, vocab) for doc in documents])
    sklearn_matrix = sklearn_cosine(vectors)
    
    print("\n📊 Our Implementation:")
    print(our_matrix)
    
    print("\n📊 Sklearn Implementation:")
    print(sklearn_matrix)
    
    print("\n✅ Difference (should be near zero):")
    print(np.abs(our_matrix - sklearn_matrix).max())


def demonstrate_similarity():
    """Demonstrate cosine similarity properties"""
    print("\n" + "="*80)
    print("DEMONSTRATING COSINE SIMILARITY PROPERTIES")
    print("="*80)
    
    # Property 1: Identical vectors
    vec1 = np.array([1, 2, 3])
    sim = cosine_similarity(vec1, vec1)
    print(f"\n1️⃣  Identical vectors similarity: {sim:.3f}")
    print(f"   Expected: 1.0 ✅")
    
    # Property 2: Orthogonal vectors
    vec2 = np.array([1, 0, 0])
    vec3 = np.array([0, 1, 0])
    sim = cosine_similarity(vec2, vec3)
    print(f"\n2️⃣  Orthogonal vectors similarity: {sim:.3f}")
    print(f"   Expected: 0.0 ✅")
    
    # Property 3: Opposite vectors
    vec4 = np.array([1, 1, 1])
    vec5 = np.array([-1, -1, -1])
    sim = cosine_similarity(vec4, vec5)
    print(f"\n3️⃣  Opposite vectors similarity: {sim:.3f}")
    print(f"   Expected: -1.0 ✅")
    
    # Property 4: Scale invariance
    vec6 = np.array([1, 2, 3])
    vec7 = np.array([2, 4, 6])  # 2x vec6
    sim = cosine_similarity(vec6, vec7)
    print(f"\n4️⃣  Scaled vector similarity: {sim:.3f}")
    print(f"   Expected: 1.0 (scale invariant!) ✅")


def analyze_document_similarity():
    """Analyze similarity between sample documents"""
    print("\n" + "="*80)
    print("ANALYZING DOCUMENT SIMILARITY")
    print("="*80)
    
    vocab = build_vocabulary(sample_docs)
    print(f"\n📚 Vocabulary size: {len(vocab)} unique words")
    
    # Calculate all pairwise similarities
    for i in range(len(sample_docs)):
        for j in range(i+1, len(sample_docs)):
            vec1 = text_to_bow_vector(sample_docs[i], vocab)
            vec2 = text_to_bow_vector(sample_docs[j], vocab)
            sim = cosine_similarity(vec1, vec2)
            
            print(f"\n📄 Document {i} vs Document {j}:")
            print(f"   '{sample_docs[i]}'")
            print(f"   '{sample_docs[j]}'")
            print(f"   Similarity: {sim:.3f}")
            
            # Explain similarity
            if sim > 0.5:
                print(f"   ✅ High similarity - many shared words")
            elif sim > 0.2:
                print(f"   ⚠️  Moderate similarity - some shared words")
            else:
                print(f"   ❌ Low similarity - few shared words")


def visualize_similarity_matrix():
    """Visualize the similarity matrix"""
    print("\n" + "="*80)
    print("SIMILARITY MATRIX VISUALIZATION")
    print("="*80)
    
    sim_matrix = calculate_similarity_matrix(sample_docs)
    
    print("\n📊 Similarity Matrix:")
    print("    ", end="")
    for i in range(len(sample_docs)):
        print(f"Doc{i}  ", end="")
    print()
    
    for i in range(len(sample_docs)):
        print(f"Doc{i}", end=" ")
        for j in range(len(sample_docs)):
            print(f"{sim_matrix[i,j]:.2f}  ", end="")
        print()
    
    print("\n💡 Reading the matrix:")
    print("   - Diagonal = 1.0 (document compared with itself)")
    print("   - Symmetric (sim(A,B) = sim(B,A))")
    print("   - Higher values = more similar documents")


def main():
    """Main demonstration"""
    print("=" * 80)
    print("TOPIC 1.2 - BEGINNER DEMO SOLUTION")
    print("Cosine Similarity from Scratch")
    print("=" * 80)
    
    # Demo 1: Properties of cosine similarity
    demonstrate_similarity()
    
    # Demo 2: Document similarity analysis
    analyze_document_similarity()
    
    # Demo 3: Similarity matrix
    visualize_similarity_matrix()
    
    # Demo 4: Compare with sklearn
    compare_with_sklearn(sample_docs)
    
    print("\n" + "="*80)
    print("✅ SOLUTION COMPLETE!")
    print("="*80)
    print("\n📚 KEY TAKEAWAYS:")
    print("1. Cosine similarity measures angle between vectors (0-1 for positive vectors)")
    print("2. Scale invariant: [1,2,3] and [2,4,6] have similarity 1.0")
    print("3. Diagonal of similarity matrix is always 1.0")
    print("4. Perfect for text similarity (order doesn't matter)")
    print("5. Fast to compute with NumPy vectorization")
    
    print("\n⚠️  WHEN NOT TO USE:")
    print("- When document length matters (use Euclidean distance)")
    print("- When zero vectors are common (undefined similarity)")
    print("- When negative values are meaningful")
    
    print("\n💡 TRY THIS:")
    print("- Compare long vs short documents with same words")
    print("- Try with normalized TF-IDF instead of raw counts")
    print("- Implement Jaccard similarity and compare")
    print("- Use with word embeddings instead of BoW")


if __name__ == "__main__":
    main()
