"""
===============================================================================
TOPIC 1.4 - BEGINNER PRACTICE 1: Bag of Words vs Word Embeddings
===============================================================================

🎯 LEARNING GOALS
-----------------
1. Understand limitations of Bag of Words
2. Learn about word embeddings and semantic meaning
3. Compare BoW and Word2Vec similarity
4. Prepare for modern NLP with embeddings

📚 KEY CONCEPTS: BoW limitations, word embeddings, semantic similarity, Word2Vec

⏱️ TIME ESTIMATE: 45-60 minutes

🔧 VS CODE SETUP
----------------
1. Open this file in VS Code
2. Terminal: cd e:/ey-ai/nlp-labs/topic-1.4-rag-genai/beginner
3. Install: pip install gensim
4. Run: python practice1_exercise.py
5. Debug: F9 (breakpoint), F5 (start)

📝 WHAT YOU NEED TO DO
----------------------
TODO 1: Implement BoW similarity calculation
        Use CountVectorizer and cosine_similarity
        
TODO 2: Train simple Word2Vec model
        Use gensim.models.Word2Vec
        
TODO 3: Implement document embedding (average word vectors)
        Average all word vectors in document
        
TODO 4: Compare BoW vs embedding similarity
        Show where BoW fails but embeddings succeed
        
TODO 5: Demonstrate semantic relationships

💡 EXPECTED OUTPUT
------------------
- BoW similarity scores
- Word2Vec similarity scores
- Examples where embeddings capture semantics better
- Word analogies (king - man + woman = queen)

Let's get started! 🚀
"""

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from typing import List, Tuple

# Sample sentences
sentences = [
    "the cat sat on the mat",
    "the dog sat on the rug",
    "the kitten played on the carpet",
    "python is a programming language",
    "java is a programming language"
]


def bow_similarity(text1: str, text2: str) -> float:
    """
    Calculate similarity using Bag of Words
    
    Args:
        text1: First text
        text2: Second text
    
    Returns:
        Cosine similarity score
    """
    # TODO: Implement BoW similarity
    # Hint:
    # 1. Create CountVectorizer
    # 2. Fit and transform both texts
    # 3. Compute cosine_similarity
    pass


def train_word2vec(sentences: List[str]):
    """
    Train Word2Vec model
    
    Args:
        sentences: List of sentences
    
    Returns:
        Trained Word2Vec model
    """
    # TODO: Implement Word2Vec training
    # Hint:
    # from gensim.models import Word2Vec
    # tokenized = [sent.split() for sent in sentences]
    # model = Word2Vec(tokenized, vector_size=50, window=5, min_count=1)
    pass


def document_to_vector(doc: str, model) -> np.ndarray:
    """
    Convert document to vector using word embeddings
    
    Args:
        doc: Document text
        model: Trained Word2Vec model
    
    Returns:
        Document vector (average of word vectors)
    """
    # TODO: Implement document vectorization
    # Hint:
    # 1. Tokenize document
    # 2. Get vector for each word from model
    # 3. Average all vectors
    pass


def embedding_similarity(text1: str, text2: str, model) -> float:
    """
    Calculate similarity using word embeddings
    
    Args:
        text1: First text
        text2: Second text
        model: Word2Vec model
    
    Returns:
        Cosine similarity score
    """
    # TODO: Implement embedding similarity
    # Hint: Convert both texts to vectors, then compute cosine similarity
    pass


def main():
    """Main execution"""
    print("=" * 80)
    print("TOPIC 1.4 - BEGINNER PRACTICE 1")
    print("Bag of Words vs Word Embeddings")
    print("=" * 80)
    print()
    
    # TODO: Compare BoW and Word2Vec similarities
    # TODO: Show semantic relationships
    # TODO: Demonstrate word analogies
    
    print("\n⚠️  Complete the TODO items above, then run this file again!")
    print("Compare your output with practice1_solution.py when done.")


if __name__ == "__main__":
    main()
