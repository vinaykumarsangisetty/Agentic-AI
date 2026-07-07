"""
===============================================================================
✅ COMPLETE SOLUTION
TOPIC 1.2 - BEGINNER PRACTICE 2: BM25 Ranking Algorithm
===============================================================================
"""

import numpy as np
from collections import Counter
from typing import List, Dict, Tuple
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

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
    """Compute Inverse Document Frequency"""
    N = len(documents)
    df = sum(1 for doc in documents if term in doc.lower().split())
    
    # BM25 IDF formula (different from standard IDF)
    idf = np.log((N - df + 0.5) / (df + 0.5) + 1)
    return idf


def compute_term_frequency(document: str, term: str) -> int:
    """Count term frequency in document"""
    words = document.lower().split()
    return Counter(words).get(term.lower(), 0)


def compute_bm25_score(
    query: str,
    document: str,
    documents: List[str],
    k1: float = 1.5,
    b: float = 0.75
) -> float:
    """Compute BM25 score"""
    # Calculate average document length
    avgdl = np.mean([len(doc.split()) for doc in documents])
    
    # Get document length
    doc_len = len(document.split())
    
    # Calculate score for each query term
    score = 0.0
    query_terms = query.lower().split()
    
    for term in query_terms:
        # Get term frequency in document
        tf = compute_term_frequency(document, term)
        
        if tf == 0:
            continue
        
        # Get IDF
        idf = compute_idf(documents, term)
        
        # BM25 formula
        numerator = tf * (k1 + 1)
        denominator = tf + k1 * (1 - b + b * (doc_len / avgdl))
        
        score += idf * (numerator / denominator)
    
    return score


class BM25Retriever:
    """BM25 retrieval system"""
    
    def __init__(self, documents: List[str], k1: float = 1.5, b: float = 0.75):
        self.documents = documents
        self.k1 = k1
        self.b = b
        self.avgdl = np.mean([len(doc.split()) for doc in documents])
    
    def rank(self, query: str, top_k: int = None) -> List[Tuple[int, float]]:
        """Rank documents for a query"""
        scores = []
        
        for doc_id, doc in enumerate(self.documents):
            score = compute_bm25_score(query, doc, self.documents, self.k1, self.b)
            scores.append((doc_id, score))
        
        # Sort by score (descending)
        scores.sort(key=lambda x: x[1], reverse=True)
        
        # Return top_k
        if top_k is not None:
            scores = scores[:top_k]
        
        return scores


def compare_with_tfidf():
    """Compare BM25 with TF-IDF ranking"""
    print("\n" + "="*80)
    print("COMPARING BM25 WITH TF-IDF")
    print("="*80)
    
    # BM25 retriever
    bm25 = BM25Retriever(documents)
    
    # TF-IDF vectorizer
    tfidf = TfidfVectorizer()
    tfidf_matrix = tfidf.fit_transform(documents)
    
    for query in queries:
        print(f"\n🔍 Query: '{query}'")
        print("-" * 40)
        
        # BM25 ranking
        bm25_results = bm25.rank(query, top_k=3)
        print("\n📊 BM25 Ranking:")
        for rank, (doc_id, score) in enumerate(bm25_results, 1):
            print(f"  {rank}. Doc {doc_id} (score={score:.3f})")
            print(f"     {documents[doc_id]}")
        
        # TF-IDF ranking
        query_vec = tfidf.transform([query])
        similarities = cosine_similarity(query_vec, tfidf_matrix)[0]
        tfidf_results = sorted(enumerate(similarities), key=lambda x: x[1], reverse=True)[:3]
        
        print("\n📊 TF-IDF Ranking:")
        for rank, (doc_id, score) in enumerate(tfidf_results, 1):
            print(f"  {rank}. Doc {doc_id} (score={score:.3f})")
            print(f"     {documents[doc_id]}")


def demonstrate_parameter_tuning():
    """Show effect of k1 and b parameters"""
    print("\n" + "="*80)
    print("PARAMETER TUNING DEMONSTRATION")
    print("="*80)
    
    query = "cat dog"
    
    # Test different k1 values (term frequency saturation)
    print("\n📊 Effect of k1 (term frequency saturation):")
    print("    Lower k1 = less emphasis on term frequency")
    print("    Higher k1 = more emphasis on term frequency\n")
    
    for k1 in [0.5, 1.5, 3.0]:
        retriever = BM25Retriever(documents, k1=k1, b=0.75)
        results = retriever.rank(query, top_k=3)
        print(f"  k1={k1}:")
        for doc_id, score in results:
            print(f"    Doc {doc_id}: {score:.3f}")
    
    # Test different b values (length normalization)
    print("\n📊 Effect of b (length normalization):")
    print("    b=0 = no length normalization")
    print("    b=1 = full length normalization\n")
    
    for b in [0.0, 0.75, 1.0]:
        retriever = BM25Retriever(documents, k1=1.5, b=b)
        results = retriever.rank(query, top_k=3)
        print(f"  b={b}:")
        for doc_id, score in results:
            print(f"    Doc {doc_id}: {score:.3f}")


def explain_bm25_formula():
    """Explain BM25 components with example"""
    print("\n" + "="*80)
    print("BM25 FORMULA EXPLAINED")
    print("="*80)
    
    query = "cat"
    doc = documents[0]
    
    print(f"\n🔍 Query: '{query}'")
    print(f"📄 Document: '{doc}'")
    
    # Calculate components
    term = "cat"
    tf = compute_term_frequency(doc, term)
    idf = compute_idf(documents, term)
    doc_len = len(doc.split())
    avgdl = np.mean([len(d.split()) for d in documents])
    
    k1 = 1.5
    b = 0.75
    
    print("\n📊 BM25 Components:")
    print(f"   Term frequency (tf): {tf}")
    print(f"   IDF: {idf:.3f}")
    print(f"   Document length: {doc_len}")
    print(f"   Average doc length: {avgdl:.2f}")
    print(f"   k1: {k1}")
    print(f"   b: {b}")
    
    # Calculate score step by step
    numerator = tf * (k1 + 1)
    denominator = tf + k1 * (1 - b + b * (doc_len / avgdl))
    tf_component = numerator / denominator
    score = idf * tf_component
    
    print("\n📐 Formula Calculation:")
    print(f"   numerator = tf * (k1 + 1) = {tf} * {k1+1} = {numerator:.3f}")
    print(f"   denominator = tf + k1*(1-b+b*|d|/avgdl)")
    print(f"               = {tf} + {k1}*(1-{b}+{b}*{doc_len}/{avgdl:.2f})")
    print(f"               = {denominator:.3f}")
    print(f"   tf_component = {numerator:.3f} / {denominator:.3f} = {tf_component:.3f}")
    print(f"   BM25 score = IDF * tf_component = {idf:.3f} * {tf_component:.3f} = {score:.3f}")


def demonstrate_ranking():
    """Demonstrate BM25 ranking for multiple queries"""
    print("\n" + "="*80)
    print("BM25 RANKING DEMONSTRATION")
    print("="*80)
    
    retriever = BM25Retriever(documents)
    
    for query in queries:
        print(f"\n🔍 Query: '{query}'")
        print("-" * 40)
        
        results = retriever.rank(query, top_k=3)
        
        if not results or results[0][1] == 0:
            print("   ❌ No relevant documents found")
            continue
        
        for rank, (doc_id, score) in enumerate(results, 1):
            print(f"\n  {rank}. Doc {doc_id} (score={score:.3f})")
            print(f"     {documents[doc_id]}")
            
            # Explain why this document ranked high
            if score > 0:
                query_terms = set(query.lower().split())
                doc_terms = set(documents[doc_id].lower().split())
                matching_terms = query_terms & doc_terms
                print(f"     ✅ Matching terms: {matching_terms}")


def analyze_bm25_properties():
    """Analyze key properties of BM25"""
    print("\n" + "="*80)
    print("BM25 PROPERTIES")
    print("="*80)
    
    print("\n1️⃣  TERM FREQUENCY SATURATION")
    print("   BM25 has diminishing returns for repeated terms")
    doc1 = "cat " * 5  # "cat" appears 5 times
    doc2 = "cat " * 20  # "cat" appears 20 times
    score1 = compute_bm25_score("cat", doc1, [doc1, doc2])
    score2 = compute_bm25_score("cat", doc2, [doc1, doc2])
    print(f"   'cat' × 5:  score = {score1:.3f}")
    print(f"   'cat' × 20: score = {score2:.3f}")
    print(f"   Ratio: {score2/score1:.2f}x (not 4x due to saturation!)")
    
    print("\n2️⃣  LENGTH NORMALIZATION")
    print("   Longer documents are penalized")
    short_doc = "cat dog"
    long_doc = "cat dog " + "word " * 50
    score_short = compute_bm25_score("cat dog", short_doc, [short_doc, long_doc])
    score_long = compute_bm25_score("cat dog", long_doc, [short_doc, long_doc])
    print(f"   Short doc: score = {score_short:.3f}")
    print(f"   Long doc:  score = {score_long:.3f}")
    print(f"   Short doc scores higher ✅")
    
    print("\n3️⃣  IDF WEIGHTING")
    print("   Rare terms get higher weight")
    common_term = "the"
    rare_term = "quick"
    idf_common = compute_idf(documents, common_term)
    idf_rare = compute_idf(documents, rare_term)
    print(f"   '{common_term}' (common): IDF = {idf_common:.3f}")
    print(f"   '{rare_term}' (rare):   IDF = {idf_rare:.3f}")
    print(f"   Rare terms valued more ✅")


def main():
    """Main demonstration"""
    print("=" * 80)
    print("TOPIC 1.2 - BEGINNER PRACTICE 2 SOLUTION")
    print("BM25 Ranking Algorithm")
    print("=" * 80)
    
    # Explain formula
    explain_bm25_formula()
    
    # Demonstrate ranking
    demonstrate_ranking()
    
    # Compare with TF-IDF
    compare_with_tfidf()
    
    # Parameter tuning
    demonstrate_parameter_tuning()
    
    # Analyze properties
    analyze_bm25_properties()
    
    print("\n" + "="*80)
    print("✅ SOLUTION COMPLETE!")
    print("="*80)
    print("\n📚 KEY TAKEAWAYS:")
    print("1. BM25 is the state-of-the-art for keyword search")
    print("2. Term frequency has diminishing returns (saturation)")
    print("3. Longer documents are penalized (length normalization)")
    print("4. Rare terms get higher IDF weights")
    print("5. k1 controls TF saturation, b controls length normalization")
    
    print("\n💡 WHEN TO USE BM25:")
    print("✅ Keyword search (exact term matching)")
    print("✅ Search engines and information retrieval")
    print("✅ Document ranking by relevance")
    print("✅ When you have many documents")
    
    print("\n⚠️  WHEN NOT TO USE BM25:")
    print("❌ Semantic search (use embeddings instead)")
    print("❌ Very short queries (cosine similarity may be better)")
    print("❌ When synonyms matter (use word2vec/BERT)")
    
    print("\n🚀 REAL-WORLD APPLICATIONS:")
    print("- Elasticsearch (default ranking algorithm)")
    print("- Apache Solr")
    print("- Search engines")
    print("- Document retrieval systems")
    
    print("\n💡 TRY THIS:")
    print("- Tune k1 and b for your specific use case")
    print("- Combine BM25 with semantic embeddings (hybrid search)")
    print("- Add query expansion with synonyms")
    print("- Implement BM25+ (improved variant)")


if __name__ == "__main__":
    main()
