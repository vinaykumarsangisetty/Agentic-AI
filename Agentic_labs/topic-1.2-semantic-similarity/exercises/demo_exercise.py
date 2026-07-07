"""
===============================================================================
TOPIC 1.2 - BEGINNER DEMO: Cosine Similarity from Scratch
===============================================================================

🎯 LEARNING GOALS
-----------------
1. Understand the cosine similarity formula and intuition
2. Implement cosine similarity using NumPy
3. Compare with sklearn's cosine_similarity function
4. Measure semantic similarity between text documents

📚 KEY CONCEPTS
---------------
Cosine similarity, dot product, vector magnitude, document similarity

⏱️ TIME ESTIMATE: 30-45 minutes

🔧 VS CODE SETUP
----------------
1. Open this file in VS Code
2. Terminal: cd e:/ey-ai/nlp-labs/topic-1.2-semantic-similarity/beginner
3. Run: python demo_exercise.py
4. Debug: F9 (breakpoint), F5 (start debugging)

📝 WHAT YOU NEED TO DO
----------------------
TODO 1: Implement cosine_similarity() calculating similarity between two vectors
        Hint: similarity = dot(v1, v2) / (||v1|| * ||v2||)
        Use np.dot() and np.linalg.norm()
        
TODO 2: Implement text_to_bow_vector() converting text to word count vector
        Hint: Use Counter to count words, create vector with vocabulary indices
        
TODO 3: Implement calculate_similarity_matrix() for multiple documents
        Hint: Compare each document pair using cosine_similarity()
        
TODO 4: Compare your implementation with sklearn
        Hint: from sklearn.metrics.pairwise import cosine_similarity

💡 EXPECTED OUTPUT
------------------
- Similarity scores between 0 and 1
- Your implementation matching sklearn's results
- Examples showing similar vs different documents
- Similarity matrix visualization

Let's get started! 🚀
"""

import numpy as np
from collections import Counter
from typing import List, Dict

# Sample documents for similarity testing
sample_docs = [
    "the cat sat on the mat",
    "the dog sat on the log",
    "cats and dogs are animals",
    "the quick brown fox jumps over the lazy dog"
]


def cosine_similarity(vec1: np.ndarray, vec2: np.ndarray) -> float:
    """
    Calculate cosine similarity between two vectors
    
    Args:
        vec1: First vector
        vec2: Second vector
    
    Returns:
        Similarity score between 0 and 1
        
    Example:
        >>> cosine_similarity(np.array([1, 2, 3]), np.array([1, 2, 3]))
        1.0  # identical vectors
    """
    # TODO: Implement this function
    # Formula: cos(θ) = (v1 · v2) / (||v1|| * ||v2||)
    # Step 1: Calculate dot product using np.dot(vec1, vec2)
    # Step 2: Calculate magnitudes using np.linalg.norm(vec1)
    # Step 3: Return dot_product / (magnitude1 * magnitude2)
    pass


def build_vocabulary(documents: List[str]) -> Dict[str, int]:
    """
    Build vocabulary from documents
    
    Args:
        documents: List of text documents
    
    Returns:
        Dictionary mapping words to indices
    """
    # TODO: Implement this function
    # Hint: Collect unique words, sort, create {word: index} mapping
    pass


def text_to_bow_vector(text: str, vocabulary: Dict[str, int]) -> np.ndarray:
    """
    Convert text to Bag-of-Words vector
    
    Args:
        text: Input text
        vocabulary: Word to index mapping
    
    Returns:
        NumPy array with word counts
    """
    # TODO: Implement this function
    # Hint: Create zero vector, count words, fill in counts
    pass


def calculate_similarity_matrix(documents: List[str]) -> np.ndarray:
    """
    Calculate pairwise similarity matrix for documents
    
    Args:
        documents: List of documents
    
    Returns:
        2D array where element [i,j] is similarity between doc i and doc j
    """
    # TODO: Implement this function
    # Hint: Build vocabulary, convert docs to vectors, calculate pairwise similarities
    pass


def main():
    """Main execution"""
    print("=" * 80)
    print("TOPIC 1.2 - BEGINNER DEMO")
    print("Cosine Similarity from Scratch")
    print("=" * 80)
    print()
    
    # TODO: Test your implementations
    # Example:
    # vocab = build_vocabulary(sample_docs)
    # vec1 = text_to_bow_vector(sample_docs[0], vocab)
    # vec2 = text_to_bow_vector(sample_docs[1], vocab)
    # sim = cosine_similarity(vec1, vec2)
    # print(f"Similarity: {sim:.3f}")
    
    print("\n⚠️  Complete the TODO items above, then run this file again!")
    print("Compare your output with demo_solution.py when done.")


if __name__ == "__main__":
    main()
