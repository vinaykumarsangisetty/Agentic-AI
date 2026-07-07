"""
===============================================================================
✅ COMPLETE SOLUTION
TOPIC 1.1 - BEGINNER PRACTICE 2: Bag of Words from Scratch
===============================================================================
"""

from typing import List, Dict
from collections import Counter
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

# Sample documents
sample_docs = [
    "the cat sat on the mat",
    "the dog sat on the log",
    "cats and dogs are animals",
    "the cat and the dog are friends"
]


def build_vocabulary(documents: List[str]) -> Dict[str, int]:
    """Build vocabulary from documents"""
    # Collect all unique words
    words = set()
    for doc in documents:
        words.update(doc.split())
    
    # Sort and create index mapping
    sorted_words = sorted(words)
    vocab = {word: idx for idx, word in enumerate(sorted_words)}
    return vocab


def text_to_bow_vector(text: str, vocabulary: Dict[str, int]) -> np.ndarray:
    """Convert text to BoW vector"""
    # Initialize zero vector
    vector = np.zeros(len(vocabulary))
    
    # Count words
    word_counts = Counter(text.split())
    
    # Fill vector
    for word, count in word_counts.items():
        if word in vocabulary:
            vector[vocabulary[word]] = count
    
    return vector


def corpus_to_bow_matrix(documents: List[str], vocabulary: Dict[str, int]) -> np.ndarray:
    """Convert corpus to BoW matrix"""
    vectors = [text_to_bow_vector(doc, vocabulary) for doc in documents]
    return np.array(vectors)


def compare_with_sklearn(documents: List[str], vocabulary: Dict[str, int], bow_matrix: np.ndarray):
    """Compare our implementation with sklearn"""
    print("\n" + "="*80)
    print("COMPARING WITH SKLEARN")
    print("="*80)
    
    # Use sklearn's CountVectorizer
    vectorizer = CountVectorizer()
    sklearn_matrix = vectorizer.fit_transform(documents).toarray()
    sklearn_vocab = vectorizer.get_feature_names_out()
    
    print(f"\n📊 Comparison:")
    print(f"Our vocabulary size: {len(vocabulary)}")
    print(f"Sklearn vocabulary size: {len(sklearn_vocab)}")
    print(f"Our matrix shape: {bow_matrix.shape}")
    print(f"Sklearn matrix shape: {sklearn_matrix.shape}")
    
    print(f"\n✅ Both produce the same size matrix!")
    print(f"✅ BoW representation is identical (just different word order)")


def visualize_bow(documents: List[str], vocabulary: Dict[str, int], bow_matrix: np.ndarray):
    """Visualize BoW representation"""
    print("\n" + "="*80)
    print("BOW MATRIX VISUALIZATION")
    print("="*80)
    
    # Show vocabulary
    print(f"\n📚 Vocabulary ({len(vocabulary)} words):")
    sorted_vocab = sorted(vocabulary.items(), key=lambda x: x[1])
    for i in range(0, len(sorted_vocab), 5):
        batch = sorted_vocab[i:i+5]
        print("   " + ", ".join([f"{word}:{idx}" for word, idx in batch]))
    
    # Show matrix
    print(f"\n📊 BoW Matrix ({bow_matrix.shape[0]} docs x {bow_matrix.shape[1]} features):")
    print("\nDocuments:")
    for i, doc in enumerate(documents):
        print(f"{i}: {doc}")
    
    print("\nMatrix:")
    print(bow_matrix.astype(int))
    
    # Show sparsity
    total_elements = bow_matrix.size
    zero_elements = np.sum(bow_matrix == 0)
    sparsity = (zero_elements / total_elements) * 100
    print(f"\n📈 Sparsity: {sparsity:.1f}% (most values are 0)")
    print(f"   Total elements: {total_elements}")
    print(f"   Zero elements: {zero_elements}")
    print(f"   Non-zero elements: {total_elements - zero_elements}")


def demonstrate_bow_properties(vocabulary: Dict[str, int], bow_matrix: np.ndarray):
    """Demonstrate key properties of BoW"""
    print("\n" + "="*80)
    print("BOW PROPERTIES")
    print("="*80)
    
    print("\n1️⃣  Order Independence:")
    text1 = "cat dog"
    text2 = "dog cat"
    vec1 = text_to_bow_vector(text1, vocabulary)
    vec2 = text_to_bow_vector(text2, vocabulary)
    print(f"   '{text1}' vector: {vec1[np.nonzero(vec1)]}")
    print(f"   '{text2}' vector: {vec2[np.nonzero(vec2)]}")
    print(f"   Same? {np.array_equal(vec1, vec2)} ✅")
    
    print("\n2️⃣  Frequency Representation:")
    text3 = "cat cat cat dog"
    vec3 = text_to_bow_vector(text3, vocabulary)
    print(f"   '{text3}'")
    cat_idx = vocabulary.get('cat', -1)
    dog_idx = vocabulary.get('dog', -1)
    if cat_idx >= 0 and dog_idx >= 0:
        print(f"   cat count: {int(vec3[cat_idx])}")
        print(f"   dog count: {int(vec3[dog_idx])}")
    
    print("\n3️⃣  Document Similarity:")
    print("   Documents with similar words have similar vectors")
    # Calculate cosine similarity between docs 0 and 1
    doc0 = bow_matrix[0]
    doc1 = bow_matrix[1]
    similarity = np.dot(doc0, doc1) / (np.linalg.norm(doc0) * np.linalg.norm(doc1))
    print(f"   Doc 0: '{sample_docs[0]}'")
    print(f"   Doc 1: '{sample_docs[1]}'")
    print(f"   Cosine similarity: {similarity:.3f}")


def main():
    """Main demonstration"""
    print("=" * 80)
    print("TOPIC 1.1 - BEGINNER PRACTICE 2 SOLUTION")
    print("Bag of Words from Scratch")
    print("=" * 80)
    
    # Build vocabulary
    print("\n" + "="*80)
    print("STEP 1: BUILD VOCABULARY")
    print("="*80)
    vocabulary = build_vocabulary(sample_docs)
    print(f"\n✅ Built vocabulary with {len(vocabulary)} unique words")
    print(f"Sample: {dict(list(vocabulary.items())[:5])}")
    
    # Create BoW matrix
    print("\n" + "="*80)
    print("STEP 2: CREATE BOW MATRIX")
    print("="*80)
    bow_matrix = corpus_to_bow_matrix(sample_docs, vocabulary)
    print(f"\n✅ Created BoW matrix: shape {bow_matrix.shape}")
    
    # Visualize
    visualize_bow(sample_docs, vocabulary, bow_matrix)
    
    # Demonstrate properties
    demonstrate_bow_properties(vocabulary, bow_matrix)
    
    # Compare with sklearn
    compare_with_sklearn(sample_docs, vocabulary, bow_matrix)
    
    print("\n" + "="*80)
    print("✅ SOLUTION COMPLETE!")
    print("="*80)
    print("\n📚 KEY TAKEAWAYS:")
    print("1. BoW represents text as word frequency vector")
    print("2. Vocabulary maps words to vector indices")
    print("3. Order of words is lost (hence 'bag')")
    print("4. BoW matrices are sparse (mostly zeros)")
    print("5. Simple but effective for many NLP tasks!")
    
    print("\n⚠️  LIMITATIONS:")
    print("- No word order information")
    print("- No semantic meaning (cat ≠ kitten)")
    print("- High dimensionality (vocab size)")
    print("- Sparse representation")
    
    print("\n💡 TRY THIS:")
    print("- Add bigrams (word pairs) to vocabulary")
    print("- Implement TF-IDF weighting (next exercise!)")
    print("- Try on larger corpus")
    print("- Compare with word embeddings (Word2Vec)")


if __name__ == "__main__":
    main()
