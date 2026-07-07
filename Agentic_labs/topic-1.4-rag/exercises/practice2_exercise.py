"""
===============================================================================
TOPIC 1.4 - BEGINNER PRACTICE 2: Simple RAG System
===============================================================================

🎯 LEARNING GOALS
-----------------
1. Understand Retrieval-Augmented Generation (RAG) concept
2. Build document store with embeddings
3. Implement semantic search retrieval
4. Combine retrieval with simple generation

📚 KEY CONCEPTS: RAG, document retrieval, semantic search, context injection

⏱️ TIME ESTIMATE: 60-75 minutes

🔧 VS CODE SETUP
----------------
1. Open this file in VS Code
2. Terminal: cd e:/ey-ai/nlp-labs/topic-1.4-rag-genai/beginner
3. Run: python practice2_exercise.py
4. Debug: F9 (breakpoint), F5 (start)

📝 WHAT YOU NEED TO DO
----------------------
TODO 1: Create document store with TF-IDF vectors
        Store documents and their vector representations
        
TODO 2: Implement semantic search retrieval
        Find most relevant documents for query
        
TODO 3: Build context from retrieved documents
        Combine top documents into context string
        
TODO 4: Generate answer using retrieved context
        Simple template-based generation
        
TODO 5: Evaluate retrieval quality

💡 EXPECTED OUTPUT
------------------
- Retrieved documents ranked by relevance
- Generated answers grounded in retrieved context
- Comparison with/without retrieval

Let's get started! 🚀
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from typing import List, Dict, Tuple
import numpy as np

# Knowledge base documents
knowledge_base = [
    {
        'id': 1,
        'text': 'Python is a high-level programming language known for its simple syntax and readability.',
        'topic': 'Python'
    },
    {
        'id': 2,
        'text': 'Machine learning is a subset of AI that enables systems to learn from data.',
        'topic': 'ML'
    },
    {
        'id': 3,
        'text': 'Natural Language Processing helps computers understand and generate human language.',
        'topic': 'NLP'
    },
    {
        'id': 4,
        'text': 'RAG combines retrieval and generation to produce grounded, factual responses.',
        'topic': 'RAG'
    },
    {
        'id': 5,
        'text': 'TF-IDF measures word importance by balancing frequency and rarity across documents.',
        'topic': 'TF-IDF'
    }
]


class SimpleRAG:
    """Simple RAG system using TF-IDF"""
    
    def __init__(self, documents: List[Dict]):
        """
        Initialize RAG system
        
        Args:
            documents: List of documents with 'text' field
        """
        # TODO: Implement initialization
        # Hint:
        # 1. Store documents
        # 2. Extract texts
        # 3. Create and fit TfidfVectorizer
        # 4. Transform documents to vectors
        pass
    
    def retrieve(self, query: str, top_k: int = 2) -> List[Tuple[Dict, float]]:
        """
        Retrieve most relevant documents
        
        Args:
            query: Search query
            top_k: Number of documents to retrieve
        
        Returns:
            List of (document, score) tuples
        """
        # TODO: Implement retrieval
        # Hint:
        # 1. Transform query with vectorizer
        # 2. Compute similarity with all documents
        # 3. Sort by score and return top_k
        pass
    
    def generate_answer(self, query: str, retrieved_docs: List[Tuple[Dict, float]]) -> str:
        """
        Generate answer using retrieved context
        
        Args:
            query: User query
            retrieved_docs: Retrieved documents with scores
        
        Returns:
            Generated answer
        """
        # TODO: Implement simple generation
        # Hint:
        # 1. Extract text from retrieved documents
        # 2. Create context string
        # 3. Use template: "Based on the context: {context}\nAnswer: {answer}"
        pass
    
    def query(self, question: str, top_k: int = 2) -> Dict:
        """
        Complete RAG query: retrieve + generate
        
        Args:
            question: User question
            top_k: Number of documents to retrieve
        
        Returns:
            Dictionary with retrieved docs and answer
        """
        # TODO: Implement complete RAG pipeline
        # Hint:
        # 1. Retrieve relevant documents
        # 2. Generate answer from retrieved context
        # 3. Return both retrieved docs and answer
        pass


def main():
    """Main execution"""
    print("=" * 80)
    print("TOPIC 1.4 - BEGINNER PRACTICE 2")
    print("Simple RAG System")
    print("=" * 80)
    print()
    
    # TODO: Initialize RAG system
    # TODO: Test with sample queries
    # TODO: Compare with/without retrieval
    # TODO: Evaluate retrieval quality
    
    print("\n⚠️  Complete the TODO items above, then run this file again!")
    print("Compare your output with practice2_solution.py when done.")


if __name__ == "__main__":
    main()
