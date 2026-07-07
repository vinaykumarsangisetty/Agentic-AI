"""
===============================================================================
TOPIC 1.2 - BEGINNER PRACTICE 1: Building an Inverted Index
===============================================================================

🎯 LEARNING GOALS
-----------------
1. Understand inverted index data structure
2. Build an inverted index from a document collection
3. Implement boolean search queries (AND, OR)
4. Compare search speed with linear scan

📚 KEY CONCEPTS
---------------
Inverted index, posting lists, boolean retrieval, search optimization

⏱️ TIME ESTIMATE: 45-60 minutes

🔧 VS CODE SETUP
----------------
1. Open this file in VS Code
2. Terminal: cd e:/ey-ai/nlp-labs/topic-1.2-semantic-similarity/beginner
3. Run: python practice1_exercise.py
4. Debug: F9 (breakpoint), F5 (debug)

📝 WHAT YOU NEED TO DO
----------------------
TODO 1: Implement build_inverted_index() creating term→document_ids mapping
        Hint: Dictionary where keys are terms, values are sets of document IDs
        
TODO 2: Implement search_term() finding documents containing a single term
        Hint: Just look up the term in the inverted index
        
TODO 3: Implement and_search() finding documents containing ALL query terms
        Hint: Use set intersection (&) on posting lists
        
TODO 4: Implement or_search() finding documents containing ANY query term
        Hint: Use set union (|) on posting lists
        
TODO 5: Compare inverted index speed with linear scan
        Hint: Time both approaches using time.time()

💡 EXPECTED OUTPUT
------------------
- Inverted index structure showing term→doc_ids
- Search results for single and multi-term queries
- Boolean AND/OR search results
- Speed comparison (inverted index should be much faster!)

Let's get started! 🚀
"""

from typing import List, Dict, Set
import time

# Sample document collection
documents = [
    "the cat sat on the mat",
    "the dog sat on the log",
    "cats and dogs are animals",
    "the quick brown fox jumps over the lazy dog",
    "all animals are equal but some animals are more equal than others"
]


def build_inverted_index(documents: List[str]) -> Dict[str, Set[int]]:
    """
    Build inverted index from documents
    
    Args:
        documents: List of text documents
    
    Returns:
        Dictionary mapping terms to sets of document IDs
        
    Example:
        >>> build_inverted_index(["cat sat", "dog sat"])
        {'cat': {0}, 'sat': {0, 1}, 'dog': {1}}
    """
    # TODO: Implement this function
    # Hint:
    # 1. Create empty dictionary: index = {}
    # 2. Loop through documents with enumerate(documents) to get doc_id
    # 3. For each word in doc.split():
    #    - If word not in index, create empty set: index[word] = set()
    #    - Add doc_id to the set: index[word].add(doc_id)
    # 4. Return index
    pass


def search_term(index: Dict[str, Set[int]], term: str) -> Set[int]:
    """
    Search for documents containing a single term
    
    Args:
        index: Inverted index
        term: Search term
    
    Returns:
        Set of document IDs containing the term
    """
    # TODO: Implement this function
    # Hint: return index.get(term, set())
    pass


def and_search(index: Dict[str, Set[int]], terms: List[str]) -> Set[int]:
    """
    Find documents containing ALL terms (boolean AND)
    
    Args:
        index: Inverted index
        terms: List of search terms
    
    Returns:
        Set of document IDs containing all terms
        
    Example:
        >>> and_search(index, ["cat", "sat"])
        {0}  # Only doc 0 contains both "cat" AND "sat"
    """
    # TODO: Implement this function
    # Hint:
    # 1. Get posting list for first term
    # 2. For each remaining term, intersect with its posting list using &
    # 3. Return the intersection
    pass


def or_search(index: Dict[str, Set[int]], terms: List[str]) -> Set[int]:
    """
    Find documents containing ANY term (boolean OR)
    
    Args:
        index: Inverted index
        terms: List of search terms
    
    Returns:
        Set of document IDs containing any of the terms
        
    Example:
        >>> or_search(index, ["cat", "dog"])
        {0, 1}  # Docs containing "cat" OR "dog"
    """
    # TODO: Implement this function
    # Hint:
    # 1. Start with empty set: result = set()
    # 2. For each term, union with its posting list using |
    # 3. Return the union
    pass


def linear_scan_search(documents: List[str], terms: List[str]) -> Set[int]:
    """
    Search documents by scanning all documents (slow method)
    
    Args:
        documents: List of documents
        terms: Search terms
    
    Returns:
        Set of document IDs containing all terms
    """
    # This one is implemented for you to compare speeds!
    result = set()
    for doc_id, doc in enumerate(documents):
        if all(term in doc for term in terms):
            result.add(doc_id)
    return result


def main():
    """Main execution"""
    print("=" * 80)
    print("TOPIC 1.2 - BEGINNER PRACTICE 1")
    print("Building an Inverted Index")
    print("=" * 80)
    print()
    
    # TODO: Test your implementations
    # Example:
    # index = build_inverted_index(documents)
    # print("Inverted Index:", index)
    # results = search_term(index, "cat")
    # print(f"Documents containing 'cat': {results}")
    
    print("\n⚠️  Complete the TODO items above, then run this file again!")
    print("Compare your output with practice1_solution.py when done.")


if __name__ == "__main__":
    main()
