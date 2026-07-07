"""
===============================================================================
TOPIC 1.4 - BEGINNER DEMO: End-to-End NLP Pipeline
===============================================================================

🎯 LEARNING GOALS
-----------------
1. Combine all learned concepts into complete pipeline
2. Process documents, extract entities, classify sentiment
3. Build document search with cosine similarity
4. Understand how NLP components work together

📚 KEY CONCEPTS: Pipeline architecture, text processing, NER, classification, search

⏱️ TIME ESTIMATE: 45-60 minutes

🔧 VS CODE SETUP
----------------
1. Open this file in VS Code
2. Terminal: cd e:/ey-ai/nlp-labs/topic-1.4-rag-genai/beginner
3. Run: python demo_exercise.py
4. Debug: F9 (breakpoint), F5 (start)

📝 WHAT YOU NEED TO DO
----------------------
TODO 1: Implement preprocess_document()
        Clean text, tokenize, remove stopwords
        
TODO 2: Implement extract_entities()
        Find emails, URLs, dates using regex
        
TODO 3: Implement classify_sentiment()
        Determine if text is positive or negative
        
TODO 4: Implement compute_similarity()
        Calculate cosine similarity between documents
        
TODO 5: Build search_documents() function

💡 EXPECTED OUTPUT
------------------
- Processed documents with entities extracted
- Sentiment classification for each document
- Search results ranked by similarity

Let's get started! 🚀
"""

import re
from typing import List, Dict, Tuple
from collections import Counter
import math

# Sample document collection
documents = [
    {
        'id': 1,
        'text': 'Contact us at support@company.com for excellent service. Visit https://company.com',
        'title': 'Customer Support'
    },
    {
        'id': 2,
        'text': 'This product is terrible and disappointing. Email complaints@company.org',
        'title': 'Negative Review'
    },
    {
        'id': 3,
        'text': 'Amazing experience! Loved it. Check https://reviews.com for more details.',
        'title': 'Positive Review'
    }
]


def preprocess_document(text: str) -> List[str]:
    """
    Preprocess document text
    
    Args:
        text: Raw document text
    
    Returns:
        List of processed tokens
    """
    # TODO: Implement preprocessing
    # Hint: lowercase, remove punctuation, tokenize, remove stopwords
    # stopwords = {'a', 'an', 'the', 'is', 'at', 'for', 'and', 'or'}
    pass


def extract_entities(text: str) -> Dict[str, List[str]]:
    """
    Extract named entities from text
    
    Args:
        text: Input text
    
    Returns:
        Dictionary of entity types and their values
    """
    # TODO: Implement entity extraction
    # Hint: Use regex patterns for emails, URLs, dates
    # Return format: {'emails': [...], 'urls': [...]}
    pass


def classify_sentiment(text: str) -> str:
    """
    Classify sentiment of text
    
    Args:
        text: Input text
    
    Returns:
        'positive' or 'negative'
    """
    # TODO: Implement simple sentiment classification
    # Hint: Count positive vs negative words
    # positive_words = {'excellent', 'amazing', 'great', 'loved', 'wonderful'}
    # negative_words = {'terrible', 'disappointing', 'awful', 'bad', 'poor'}
    pass


def compute_similarity(doc1_tokens: List[str], doc2_tokens: List[str]) -> float:
    """
    Compute cosine similarity between documents
    
    Args:
        doc1_tokens: Tokens from document 1
        doc2_tokens: Tokens from document 2
    
    Returns:
        Cosine similarity score (0-1)
    """
    # TODO: Implement cosine similarity
    # Hint: Use counter to create vectors, then compute cosine
    pass


def search_documents(query: str, documents: List[Dict], top_k: int = 3) -> List[Tuple[Dict, float]]:
    """
    Search documents by similarity to query
    
    Args:
        query: Search query
        documents: List of documents
        top_k: Number of results to return
    
    Returns:
        List of (document, score) tuples ranked by relevance
    """
    # TODO: Implement document search
    # Hint: Process query, compute similarity with each doc, sort by score
    pass


def main():
    """Main execution"""
    print("=" * 80)
    print("TOPIC 1.4 - BEGINNER DEMO")
    print("End-to-End NLP Pipeline")
    print("=" * 80)
    print()
    
    # TODO: Process all documents
    # TODO: Extract entities from each document
    # TODO: Classify sentiment for each document
    # TODO: Perform search queries
    
    print("\n⚠️  Complete the TODO items above, then run this file again!")
    print("Compare your output with demo_solution.py when done.")


if __name__ == "__main__":
    main()
