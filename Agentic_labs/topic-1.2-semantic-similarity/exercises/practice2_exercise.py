"""
===============================================================================
TOPIC 1.2 - BEGINNER PRACTICE 2: BM25 Ranking Algorithm
===============================================================================

🎯 LEARNING GOALS
-----------------
1. Understand the BM25 ranking formula and its components
2. Implement BM25 from scratch with NumPy
3. Compare BM25 with TF-IDF ranking
4. Learn how to tune k1 and b parameters

📚 KEY CONCEPTS
---------------
BM25, term frequency saturation, document length normalization, IDF, ranking

⏱️ TIME ESTIMATE: 60-75 minutes

🔧 VS CODE SETUP
----------------
1. Open this file in VS Code
2. Terminal: cd e:/ey-ai/nlp-labs/topic-1.2-semantic-similarity/beginner
3. Run: python practice2_exercise.py
4. Debug: F9 (breakpoint), F5 (debug)

📝 WHAT YOU NEED TO DO
----------------------
TODO 1: Implement compute_idf() calculating inverse document frequency
        Hint: IDF(term) = log((N - df + 0.5) / (df + 0.5) + 1)
        where N = total docs, df = docs containing term
        
TODO 2: Implement compute_term_frequency() counting term occurrences in doc
        Hint: Use Counter or simple dictionary
        
TODO 3: Implement compute_bm25_score() calculating BM25 score
        Formula: BM25(q,d) = Σ IDF(qi) * (f(qi,d) * (k1+1)) / (f(qi,d) + k1*(1-b+b*|d|/avgdl))
        where:
        - f(qi,d) = frequency of query term qi in document d
        - |d| = length of document d
        - avgdl = average document length
        - k1 = term frequency saturation (default 1.5)
        - b = document length normalization (default 0.75)
        
TODO 4: Implement BM25Retriever class to rank documents for queries
        
TODO 5: Compare BM25 with TF-IDF ranking
        Hint: Use sklearn's TfidfVectorizer for comparison

💡 EXPECTED OUTPUT
------------------
- BM25 scores for query-document pairs
- Ranked list of documents for queries
- Comparison with TF-IDF ranking
- Effect of parameter tuning on results

Let's get started! 🚀
"""

import numpy as np
from collections import Counter
from typing import List, Dict, Tuple

# Sample document collection
documents = [
    "the cat sat on the mat",
    "the dog sat on the log",
    "cats and dogs are animals",
    "the quick brown fox jumps over the lazy dog",
    "all animals are equal but some animals are more equal than others",
    "the cat and the dog are friends"
]

# Sample queries
queries = [
    "cat dog",
    "animals equal",
    "quick fox"
]


def compute_idf(documents: List[str], term: str) -> float:
    """
    Compute Inverse Document Frequency for a term
    
    Args:
        documents: List of documents
        term: Term to compute IDF for
    
    Returns:
        IDF score
        
    Formula: IDF(t) = log((N - df + 0.5) / (df + 0.5) + 1)
    where N = total documents, df = documents containing term
    """
    # TODO: Implement this function
    # Hint:
    # 1. N = len(documents)
    # 2. Count how many documents contain the term (df)
    # 3. Apply the formula above using np.log()
    pass


def compute_term_frequency(document: str, term: str) -> int:
    """
    Count how many times a term appears in a document
    
    Args:
        document: Text document
        term: Term to count
    
    Returns:
        Frequency count
    """
    # TODO: Implement this function
    # Hint: Use Counter(document.split()).get(term, 0)
    pass


def compute_bm25_score(
    query: str,
    document: str,
    documents: List[str],
    k1: float = 1.5,
    b: float = 0.75
) -> float:
    """
    Compute BM25 score for a query-document pair
    
    Args:
        query: Search query
        document: Document to score
        documents: All documents (for IDF and avgdl)
        k1: Term frequency saturation parameter (default 1.5)
        b: Document length normalization parameter (default 0.75)
    
    Returns:
        BM25 score
        
    Formula:
    BM25(q,d) = Σ IDF(qi) * (f(qi,d) * (k1+1)) / (f(qi,d) + k1*(1-b+b*|d|/avgdl))
    """
    # TODO: Implement this function
    # Hint:
    # 1. Calculate average document length (avgdl)
    # 2. Get document length (doc_len = len(document.split()))
    # 3. For each query term:
    #    - Get term frequency f(qi,d)
    #    - Get IDF(qi)
    #    - Apply BM25 formula
    # 4. Sum scores for all query terms
    pass


class BM25Retriever:
    """BM25 retrieval system"""
    
    def __init__(self, documents: List[str], k1: float = 1.5, b: float = 0.75):
        """
        Initialize BM25 retriever
        
        Args:
            documents: Document collection
            k1: Term frequency saturation
            b: Length normalization
        """
        self.documents = documents
        self.k1 = k1
        self.b = b
        # TODO: Precompute average document length
        # self.avgdl = ...
    
    def rank(self, query: str, top_k: int = None) -> List[Tuple[int, float]]:
        """
        Rank documents for a query
        
        Args:
            query: Search query
            top_k: Return top k results (None = all)
        
        Returns:
            List of (doc_id, score) tuples, sorted by score
        """
        # TODO: Implement this method
        # Hint:
        # 1. Calculate BM25 score for each document
        # 2. Sort by score (descending)
        # 3. Return top_k results
        pass


def main():
    """Main execution"""
    print("=" * 80)
    print("TOPIC 1.2 - BEGINNER PRACTICE 2")
    print("BM25 Ranking Algorithm")
    print("=" * 80)
    print()
    
    # TODO: Test your implementations
    # Example:
    # retriever = BM25Retriever(documents)
    # query = "cat dog"
    # results = retriever.rank(query, top_k=3)
    # for doc_id, score in results:
    #     print(f"Doc {doc_id} (score={score:.3f}): {documents[doc_id]}")
    
    print("\n⚠️  Complete the TODO items above, then run this file again!")
    print("Compare your output with practice2_solution.py when done.")


if __name__ == "__main__":
    main()
