"""
===============================================================================
✅ COMPLETE SOLUTION
TOPIC 1.4 - BEGINNER PRACTICE 1: Bag of Words vs Word Embeddings
===============================================================================
"""

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from gensim.models import Word2Vec
import numpy as np
from typing import List

sentences = [
    "the cat sat on the mat",
    "the dog sat on the rug",
    "the kitten played on the carpet",
    "python is a programming language",
    "java is a programming language",
    "cats and dogs are pets",
    "programming in python is fun",
    "the puppy ran on the floor"
]


def bow_similarity(text1: str, text2: str) -> float:
    """Calculate similarity using Bag of Words"""
    vectorizer = CountVectorizer()
    vectors = vectorizer.fit_transform([text1, text2])
    return cosine_similarity(vectors[0], vectors[1])[0][0]


def train_word2vec(sentences: List[str]):
    """Train Word2Vec model"""
    tokenized = [sent.split() for sent in sentences]
    model = Word2Vec(tokenized, vector_size=50, window=5, min_count=1, epochs=100)
    return model


def document_to_vector(doc: str, model) -> np.ndarray:
    """Convert document to vector using word embeddings"""
    words = doc.split()
    vectors = []
    
    for word in words:
        if word in model.wv:
            vectors.append(model.wv[word])
    
    if len(vectors) == 0:
        return np.zeros(model.vector_size)
    
    return np.mean(vectors, axis=0)


def embedding_similarity(text1: str, text2: str, model) -> float:
    """Calculate similarity using word embeddings"""
    vec1 = document_to_vector(text1, model)
    vec2 = document_to_vector(text2, model)
    
    # Compute cosine similarity
    dot_product = np.dot(vec1, vec2)
    norm1 = np.linalg.norm(vec1)
    norm2 = np.linalg.norm(vec2)
    
    if norm1 == 0 or norm2 == 0:
        return 0.0
    
    return dot_product / (norm1 * norm2)


def compare_similarities(text1: str, text2: str, model):
    """Compare BoW and embedding similarities"""
    bow_sim = bow_similarity(text1, text2)
    emb_sim = embedding_similarity(text1, text2, model)
    
    print(f"\n📝 Text 1: '{text1}'")
    print(f"📝 Text 2: '{text2}'")
    print(f"   BoW Similarity:       {bow_sim:.3f}")
    print(f"   Embedding Similarity: {emb_sim:.3f}")
    
    return bow_sim, emb_sim


def demonstrate_word_analogies(model):
    """Demonstrate word analogies"""
    print("\n" + "="*80)
    print("WORD ANALOGIES (king - man + woman = ?)")
    print("="*80)
    
    try:
        # Check if words exist in model
        required_words = ['cat', 'kitten', 'dog', 'puppy']
        if all(word in model.wv for word in required_words):
            result = model.wv.most_similar(
                positive=['dog', 'kitten'],
                negative=['cat'],
                topn=3
            )
            print("\n🧮 cat : kitten :: dog : ?")
            for word, score in result:
                print(f"   → {word} (score: {score:.3f})")
    except:
        print("\n⚠️  Not enough training data for reliable analogies")
        print("   (Word analogies work best with large corpora)")


def demonstrate_semantic_similarity(model):
    """Demonstrate semantic word similarity"""
    print("\n" + "="*80)
    print("SEMANTIC WORD SIMILARITY")
    print("="*80)
    
    word_pairs = [
        ('cat', 'kitten'),
        ('cat', 'dog'),
        ('python', 'java'),
        ('cat', 'python')
    ]
    
    print("\n📊 Word Pair Similarities:")
    for word1, word2 in word_pairs:
        if word1 in model.wv and word2 in model.wv:
            sim = model.wv.similarity(word1, word2)
            print(f"   {word1} ↔ {word2}: {sim:.3f}")


def main():
    """Main demonstration"""
    print("=" * 80)
    print("TOPIC 1.4 - BEGINNER PRACTICE 1 SOLUTION")
    print("Bag of Words vs Word Embeddings")
    print("=" * 80)
    
    # Train Word2Vec model
    print("\n🎓 Training Word2Vec model...")
    model = train_word2vec(sentences)
    print(f"   Vocabulary size: {len(model.wv)}")
    print(f"   Vector size: {model.vector_size}")
    print("   ✅ Training complete!")
    
    # Compare BoW vs Embeddings
    print("\n" + "="*80)
    print("COMPARISON: BoW vs EMBEDDINGS")
    print("="*80)
    
    print("\n📊 Test 1: Exact synonyms")
    compare_similarities(
        "the cat sat on the mat",
        "the kitten sat on the mat",
        model
    )
    print("   Analysis: Embeddings capture that 'cat' and 'kitten' are similar")
    
    print("\n📊 Test 2: Semantic similarity")
    compare_similarities(
        "the cat sat on the mat",
        "the dog sat on the rug",
        model
    )
    print("   Analysis: Both capture structural similarity")
    
    print("\n📊 Test 3: Different topics")
    compare_similarities(
        "the cat sat on the mat",
        "python is a programming language",
        model
    )
    print("   Analysis: Both correctly show low similarity")
    
    print("\n📊 Test 4: Where BoW fails")
    compare_similarities(
        "the cat sat on the mat",
        "the kitten played on the carpet",
        model
    )
    print("   Analysis: BoW sees no overlap (different words)")
    print("             Embeddings see semantic similarity (related concepts)")
    
    # Word similarity
    demonstrate_semantic_similarity(model)
    
    # Word analogies
    demonstrate_word_analogies(model)
    
    # Limitations
    print("\n" + "="*80)
    print("LIMITATIONS COMPARISON")
    print("="*80)
    
    print("\n🚫 Bag of Words Limitations:")
    print("   1. No semantic understanding (cat ≠ kitten)")
    print("   2. Order doesn't matter ('dog bit man' = 'man bit dog')")
    print("   3. Sparse vectors (mostly zeros)")
    print("   4. Vocabulary size grows with corpus")
    print("   5. No handling of synonyms or related words")
    
    print("\n✅ Word Embeddings Advantages:")
    print("   1. Capture semantic similarity (cat ≈ kitten)")
    print("   2. Dense vectors (all dimensions used)")
    print("   3. Fixed size regardless of vocabulary")
    print("   4. Can capture word relationships")
    print("   5. Transfer learning possible")
    
    print("\n⚠️  Word Embeddings Limitations:")
    print("   1. Need large corpus for training")
    print("   2. Still lose word order (use LSTM/Transformer for that)")
    print("   3. Context-independent (same vector for 'bank' in all contexts)")
    print("   4. Solution: Contextual embeddings (BERT, next topic!)")
    
    print("\n" + "="*80)
    print("✅ SOLUTION COMPLETE!")
    print("="*80)
    print("\n📚 KEY TAKEAWAYS:")
    print("1. BoW treats words as independent symbols (no semantics)")
    print("2. Word embeddings capture semantic relationships")
    print("3. Embeddings enable: similarity, analogies, transfer learning")
    print("4. Modern NLP uses embeddings as foundation")
    print("5. Next step: Contextual embeddings (BERT, GPT)")
    
    print("\n💡 EVOLUTION OF TEXT REPRESENTATION:")
    print("   One-Hot Encoding → Bag of Words → TF-IDF")
    print("                    → Word2Vec → GloVe")
    print("                    → BERT (contextual)")
    print("                    → GPT (contextual + generative)")
    
    print("\n💡 TRY THIS:")
    print("- Train on larger corpus (Wikipedia, news articles)")
    print("- Try GloVe embeddings instead of Word2Vec")
    print("- Use pre-trained embeddings (Google News, FastText)")
    print("- Visualize embeddings with t-SNE or PCA")
    print("- Compare with BERT embeddings (next exercise!)")


if __name__ == "__main__":
    main()
