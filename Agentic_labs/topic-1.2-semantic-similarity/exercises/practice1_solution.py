"""
===============================================================================
✅ COMPLETE SOLUTION
TOPIC 1.2 - BEGINNER PRACTICE 1: Building an Inverted Index
===============================================================================
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
    """Build inverted index from documents"""
    index = {}
    
    for doc_id, doc in enumerate(documents):
        words = doc.lower().split()
        for word in words:
            if word not in index:
                index[word] = set()
            index[word].add(doc_id)
    
    return index


def search_term(index: Dict[str, Set[int]], term: str) -> Set[int]:
    """Search for documents containing a single term"""
    return index.get(term.lower(), set())


def and_search(index: Dict[str, Set[int]], terms: List[str]) -> Set[int]:
    """Find documents containing ALL terms (boolean AND)"""
    if not terms:
        return set()
    
    # Start with posting list of first term
    result = search_term(index, terms[0])
    
    # Intersect with posting lists of remaining terms
    for term in terms[1:]:
        result = result & search_term(index, term)
    
    return result


def or_search(index: Dict[str, Set[int]], terms: List[str]) -> Set[int]:
    """Find documents containing ANY term (boolean OR)"""
    result = set()
    
    for term in terms:
        result = result | search_term(index, term)
    
    return result


def linear_scan_search(documents: List[str], terms: List[str]) -> Set[int]:
    """Search documents by scanning all (slow method)"""
    result = set()
    for doc_id, doc in enumerate(documents):
        doc_lower = doc.lower()
        if all(term.lower() in doc_lower for term in terms):
            result.add(doc_id)
    return result


def visualize_index(index: Dict[str, Set[int]], max_terms: int = 10):
    """Visualize inverted index structure"""
    print("\n" + "="*80)
    print("INVERTED INDEX STRUCTURE")
    print("="*80)
    
    print(f"\n📚 Index contains {len(index)} unique terms")
    print(f"\nShowing first {max_terms} terms:\n")
    
    for i, (term, doc_ids) in enumerate(sorted(index.items())[:max_terms]):
        print(f"'{term}' → {sorted(doc_ids)}")
    
    if len(index) > max_terms:
        print(f"\n... and {len(index) - max_terms} more terms")


def demonstrate_searches(index: Dict[str, Set[int]]):
    """Demonstrate different search types"""
    print("\n" + "="*80)
    print("SEARCH DEMONSTRATIONS")
    print("="*80)
    
    # Single term search
    print("\n1️⃣  SINGLE TERM SEARCH")
    print("-" * 40)
    term = "cat"
    results = search_term(index, term)
    print(f"Search: '{term}'")
    print(f"Results: {sorted(results)}")
    for doc_id in sorted(results):
        print(f"  Doc {doc_id}: {documents[doc_id]}")
    
    # AND search
    print("\n2️⃣  AND SEARCH (all terms must match)")
    print("-" * 40)
    terms = ["the", "dog"]
    results = and_search(index, terms)
    print(f"Search: {' AND '.join(terms)}")
    print(f"Results: {sorted(results)}")
    for doc_id in sorted(results):
        print(f"  Doc {doc_id}: {documents[doc_id]}")
    
    # OR search
    print("\n3️⃣  OR SEARCH (any term matches)")
    print("-" * 40)
    terms = ["cat", "fox"]
    results = or_search(index, terms)
    print(f"Search: {' OR '.join(terms)}")
    print(f"Results: {sorted(results)}")
    for doc_id in sorted(results):
        print(f"  Doc {doc_id}: {documents[doc_id]}")
    
    # Complex boolean search
    print("\n4️⃣  COMPLEX SEARCH")
    print("-" * 40)
    terms = ["animals", "equal"]
    results = and_search(index, terms)
    print(f"Search: {' AND '.join(terms)}")
    print(f"Results: {sorted(results)}")
    if results:
        for doc_id in sorted(results):
            print(f"  Doc {doc_id}: {documents[doc_id]}")
    else:
        print("  No documents match all terms")


def compare_performance(index: Dict[str, Set[int]]):
    """Compare inverted index vs linear scan performance"""
    print("\n" + "="*80)
    print("PERFORMANCE COMPARISON")
    print("="*80)
    
    search_queries = [
        ["cat"],
        ["the", "dog"],
        ["animals", "equal"],
        ["the", "and", "are"]
    ]
    
    for query in search_queries:
        print(f"\n🔍 Query: {' AND '.join(query)}")
        
        # Inverted index search
        start = time.time()
        for _ in range(1000):  # Run 1000 times for measurable time
            result_index = and_search(index, query)
        time_index = (time.time() - start) * 1000  # Convert to ms
        
        # Linear scan search
        start = time.time()
        for _ in range(1000):
            result_scan = linear_scan_search(documents, query)
        time_scan = (time.time() - start) * 1000
        
        # Results
        print(f"   Inverted Index: {time_index:.3f} ms")
        print(f"   Linear Scan:    {time_scan:.3f} ms")
        print(f"   ⚡ Speedup:      {time_scan/time_index:.1f}x faster")
        print(f"   ✅ Results match: {result_index == result_scan}")


def analyze_index_statistics(index: Dict[str, Set[int]]):
    """Analyze inverted index statistics"""
    print("\n" + "="*80)
    print("INDEX STATISTICS")
    print("="*80)
    
    total_terms = len(index)
    total_postings = sum(len(doc_ids) for doc_ids in index.values())
    avg_postings = total_postings / total_terms if total_terms > 0 else 0
    
    print(f"\n📊 Statistics:")
    print(f"   Total unique terms: {total_terms}")
    print(f"   Total postings: {total_postings}")
    print(f"   Average docs per term: {avg_postings:.2f}")
    print(f"   Total documents: {len(documents)}")
    
    # Find most common terms
    sorted_by_freq = sorted(index.items(), key=lambda x: len(x[1]), reverse=True)
    print(f"\n📈 Most common terms:")
    for term, doc_ids in sorted_by_freq[:5]:
        print(f"   '{term}': appears in {len(doc_ids)} documents")
    
    # Find rarest terms
    print(f"\n📉 Rarest terms (appear in 1 doc only):")
    rare_terms = [(term, doc_ids) for term, doc_ids in index.items() if len(doc_ids) == 1]
    for term, doc_ids in rare_terms[:5]:
        print(f"   '{term}': {doc_ids}")


def main():
    """Main demonstration"""
    print("=" * 80)
    print("TOPIC 1.2 - BEGINNER PRACTICE 1 SOLUTION")
    print("Building an Inverted Index")
    print("=" * 80)
    
    # Build index
    print("\n" + "="*80)
    print("BUILDING INVERTED INDEX")
    print("="*80)
    print(f"\n📚 Processing {len(documents)} documents...")
    
    index = build_inverted_index(documents)
    print(f"✅ Index built with {len(index)} unique terms")
    
    # Visualize index
    visualize_index(index)
    
    # Demonstrate searches
    demonstrate_searches(index)
    
    # Compare performance
    compare_performance(index)
    
    # Statistics
    analyze_index_statistics(index)
    
    print("\n" + "="*80)
    print("✅ SOLUTION COMPLETE!")
    print("="*80)
    print("\n📚 KEY TAKEAWAYS:")
    print("1. Inverted index maps terms to document IDs (like book index)")
    print("2. Extremely fast for keyword search (O(1) lookup)")
    print("3. Boolean AND = set intersection, OR = set union")
    print("4. Much faster than linear scan for large collections")
    print("5. Foundation of search engines (Google, Elasticsearch)")
    
    print("\n💡 REAL-WORLD APPLICATIONS:")
    print("- Search engines (Google, Bing)")
    print("- Database systems (full-text search)")
    print("- Document management systems")
    print("- Log analysis and monitoring")
    
    print("\n🚀 EXTENSIONS:")
    print("- Add positional information for phrase search")
    print("- Store term frequencies for ranking")
    print("- Implement NOT operation (set difference)")
    print("- Add stemming/lemmatization")
    print("- Support wildcard queries")


if __name__ == "__main__":
    main()
