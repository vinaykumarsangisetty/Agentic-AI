"""
===============================================================================
TOPIC 1.1 - BEGINNER PRACTICE 2: Bag of Words from Scratch
===============================================================================

🎯 LEARNING GOALS
-----------------
1. Understand Bag of Words (BoW) representation
2. Build a vocabulary from a document collection
3. Convert documents to BoW vectors
4. Compare your implementation with sklearn's CountVectorizer

📚 KEY CONCEPTS
---------------
Bag of Words, vocabulary, document vectorization, sparse representations

⏱️ TIME ESTIMATE: 45-60 minutes

🔧 VS CODE SETUP
----------------
1. Open this file in VS Code
2. Terminal: cd e:/ey-ai/nlp-labs/topic-1.1-text-preprocessing/beginner
3. Run: python practice2_exercise.py
4. Debug: F9 (breakpoint), F5 (start debugging)

📝 WHAT YOU NEED TO DO
----------------------
TODO 1: Implement build_vocabulary() - create vocab from all documents
        Hint: Use set() to collect unique words from all documents
        
TODO 2: Implement text_to_bow_vector() - convert text to word count vector
        Hint: Use Counter to count words, then map to vocabulary indices
        
TODO 3: Implement corpus_to_bow_matrix() - convert multiple docs to matrix
        Hint: Call text_to_bow_vector() for each document
        
TODO 4: Compare with sklearn's CountVectorizer
        Hint: from sklearn.feature_extraction.text import CountVectorizer

💡 EXPECTED OUTPUT
------------------
- Vocabulary listing (word → index mapping)
- BoW vectors for each document
- Side-by-side comparison of your implementation vs sklearn
- Sparse vs dense representation comparison

Let's get started! 🚀
"""

from typing import List, Dict, Tuple
from collections import Counter
import numpy as np

# Sample documents for BoW demonstration
sample_docs = [
    "the cat sat on the mat",
    "the dog sat on the log",
    "cats and dogs are animals",
    "the cat and the dog are friends"
]


def build_vocabulary(documents: List[str]) -> Dict[str, int]:
    """
    Build vocabulary from documents
    
    Args:
        documents: List of text documents
    
    Returns:
        Dictionary mapping words to indices
        
    Example:
        >>> build_vocabulary(["hello world", "world peace"])
        {'hello': 0, 'world': 1, 'peace': 2}
    """
    # TODO: Implement this function
    # Hint:
    # 1. Create empty set to collect unique words
    # 2. Loop through documents and split into words
    # 3. Add all words to set
    # 4. Sort words and create {word: index} dictionary
    pass


def text_to_bow_vector(text: str, vocabulary: Dict[str, int]) -> np.ndarray:
    """
    Convert text to BoW vector using vocabulary
    
    Args:
        text: Input text
        vocabulary: Word to index mapping
    
    Returns:
        NumPy array with word counts (length = vocab size)
        
    Example:
        >>> vocab = {'cat': 0, 'dog': 1, 'sat': 2}
        >>> text_to_bow_vector("cat sat cat", vocab)
        array([2, 0, 1])  # cat appears 2x, dog 0x, sat 1x
    """
    # TODO: Implement this function
    # Hint:
    # 1. Create zero vector of length vocabulary size
    # 2. Split text into words
    # 3. Count words using Counter
    # 4. For each word in vocabulary, set vector[index] = count
    pass


def corpus_to_bow_matrix(documents: List[str], vocabulary: Dict[str, int]) -> np.ndarray:
    """
    Convert corpus to BoW matrix
    
    Args:
        documents: List of documents
        vocabulary: Word to index mapping
    
    Returns:
        2D NumPy array (num_docs x vocab_size)
        
    Example:
        >>> vocab = {'cat': 0, 'dog': 1}
        >>> corpus_to_bow_matrix(["cat cat", "dog cat"], vocab)
        array([[2, 0],
               [1, 1]])
    """
    # TODO: Implement this function
    # Hint: Stack vectors from text_to_bow_vector() for each document
    pass


def main():
    """Main execution"""
    print("=" * 80)
    print("TOPIC 1.1 - BEGINNER PRACTICE 2")
    print("Bag of Words from Scratch")
    print("=" * 80)
    print()
    
    # TODO: Test your implementations
    # Example:
    # vocab = build_vocabulary(sample_docs)
    # print(f"Vocabulary: {vocab}")
    # matrix = corpus_to_bow_matrix(sample_docs, vocab)
    # print(f"BoW Matrix:\n{matrix}")
    
    print("\n⚠️  Complete the TODO items above, then run this file again!")
    print("Compare your output with practice2_solution.py when done.")


if __name__ == "__main__":
    main()
