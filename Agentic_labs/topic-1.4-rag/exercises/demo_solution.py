"""
===============================================================================
✅ COMPLETE SOLUTION
TOPIC 1.4 - BEGINNER DEMO: End-to-End NLP Pipeline
===============================================================================
"""

import re
from typing import List, Dict, Tuple
from collections import Counter
import math

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
    """Preprocess document text"""
    # Lowercase
    text = text.lower()
    # Remove punctuation
    text = re.sub(r'[^\w\s]', ' ', text)
    # Tokenize
    tokens = text.split()
    # Remove stopwords
    stopwords = {'a', 'an', 'the', 'is', 'at', 'for', 'and', 'or', 'it', 'us', 'to'}
    tokens = [t for t in tokens if t not in stopwords]
    return tokens


def extract_entities(text: str) -> Dict[str, List[str]]:
    """Extract named entities from text"""
    entities = {
        'emails': re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text),
        'urls': re.findall(r'https?://[^\s]+', text),
        'dates': re.findall(r'\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b', text)
    }
    return entities


def classify_sentiment(text: str) -> str:
    """Classify sentiment of text"""
    text_lower = text.lower()
    positive_words = {'excellent', 'amazing', 'great', 'loved', 'wonderful', 'fantastic', 'experience'}
    negative_words = {'terrible', 'disappointing', 'awful', 'bad', 'poor', 'worst'}
    
    pos_count = sum(1 for word in positive_words if word in text_lower)
    neg_count = sum(1 for word in negative_words if word in text_lower)
    
    return 'positive' if pos_count > neg_count else 'negative'


def compute_similarity(doc1_tokens: List[str], doc2_tokens: List[str]) -> float:
    """Compute cosine similarity between documents"""
    # Create vocabulary
    vocab = set(doc1_tokens + doc2_tokens)
    
    # Create vectors
    vec1 = Counter(doc1_tokens)
    vec2 = Counter(doc2_tokens)
    
    # Compute dot product
    dot_product = sum(vec1[word] * vec2[word] for word in vocab)
    
    # Compute magnitudes
    mag1 = math.sqrt(sum(count ** 2 for count in vec1.values()))
    mag2 = math.sqrt(sum(count ** 2 for count in vec2.values()))
    
    # Compute cosine similarity
    if mag1 == 0 or mag2 == 0:
        return 0.0
    
    return dot_product / (mag1 * mag2)


def search_documents(query: str, documents: List[Dict], top_k: int = 3) -> List[Tuple[Dict, float]]:
    """Search documents by similarity to query"""
    # Preprocess query
    query_tokens = preprocess_document(query)
    
    # Compute similarity with each document
    results = []
    for doc in documents:
        doc_tokens = preprocess_document(doc['text'])
        similarity = compute_similarity(query_tokens, doc_tokens)
        results.append((doc, similarity))
    
    # Sort by similarity
    results.sort(key=lambda x: x[1], reverse=True)
    
    # Return top k
    return results[:top_k]


def process_document_pipeline(doc: Dict) -> Dict:
    """Process single document through entire pipeline"""
    processed = {
        'id': doc['id'],
        'title': doc['title'],
        'original_text': doc['text'],
        'tokens': preprocess_document(doc['text']),
        'entities': extract_entities(doc['text']),
        'sentiment': classify_sentiment(doc['text'])
    }
    return processed


def main():
    """Main demonstration"""
    print("=" * 80)
    print("TOPIC 1.4 - BEGINNER DEMO SOLUTION")
    print("End-to-End NLP Pipeline")
    print("=" * 80)
    
    # Process all documents
    print("\n" + "="*80)
    print("PROCESSING DOCUMENTS")
    print("="*80)
    
    processed_docs = []
    for doc in documents:
        print(f"\n📄 Document {doc['id']}: {doc['title']}")
        print(f"   Original: {doc['text']}")
        
        processed = process_document_pipeline(doc)
        processed_docs.append(processed)
        
        print(f"   Tokens: {processed['tokens']}")
        print(f"   Entities:")
        for entity_type, entities in processed['entities'].items():
            if entities:
                print(f"      {entity_type}: {entities}")
        print(f"   Sentiment: {processed['sentiment'].upper()}")
    
    # Document statistics
    print("\n" + "="*80)
    print("DOCUMENT STATISTICS")
    print("="*80)
    
    total_tokens = sum(len(doc['tokens']) for doc in processed_docs)
    total_entities = sum(
        sum(len(entities) for entities in doc['entities'].values())
        for doc in processed_docs
    )
    positive_docs = sum(1 for doc in processed_docs if doc['sentiment'] == 'positive')
    
    print(f"\n📊 Collection Statistics:")
    print(f"   Total documents: {len(processed_docs)}")
    print(f"   Total tokens: {total_tokens}")
    print(f"   Total entities: {total_entities}")
    print(f"   Positive sentiment: {positive_docs}/{len(processed_docs)}")
    print(f"   Negative sentiment: {len(processed_docs) - positive_docs}/{len(processed_docs)}")
    
    # Document search
    print("\n" + "="*80)
    print("DOCUMENT SEARCH")
    print("="*80)
    
    queries = [
        "excellent customer service",
        "terrible product experience",
        "company contact information"
    ]
    
    for query in queries:
        print(f"\n🔍 Query: '{query}'")
        results = search_documents(query, documents, top_k=2)
        
        for rank, (doc, score) in enumerate(results, 1):
            print(f"   {rank}. {doc['title']} (score: {score:.3f})")
            print(f"      {doc['text'][:60]}...")
    
    # Demonstrate similarity matrix
    print("\n" + "="*80)
    print("DOCUMENT SIMILARITY MATRIX")
    print("="*80)
    
    print("\n📊 Pairwise Document Similarities:")
    for i, doc1 in enumerate(processed_docs):
        for j, doc2 in enumerate(processed_docs):
            if i < j:
                sim = compute_similarity(doc1['tokens'], doc2['tokens'])
                print(f"   Doc {doc1['id']} vs Doc {doc2['id']}: {sim:.3f}")
    
    print("\n" + "="*80)
    print("✅ SOLUTION COMPLETE!")
    print("="*80)
    print("\n📚 KEY TAKEAWAYS:")
    print("1. NLP pipeline combines: preprocessing → entity extraction → classification")
    print("2. Each component builds on previous ones")
    print("3. Document search uses vectorization + cosine similarity")
    print("4. Pipeline can be extended with more sophisticated models")
    print("5. This is foundation for building RAG systems!")
    
    print("\n💡 PIPELINE ARCHITECTURE:")
    print("   Raw Text → Preprocessing → Tokenization")
    print("            ↓")
    print("   Entity Extraction (NER)")
    print("            ↓")
    print("   Sentiment Classification")
    print("            ↓")
    print("   Vectorization → Search/Retrieval")
    
    print("\n💡 TRY THIS:")
    print("- Add more documents to the collection")
    print("- Implement TF-IDF instead of raw counts")
    print("- Add more entity types (phone numbers, addresses)")
    print("- Use spaCy for better NER")
    print("- Build a simple chatbot using this pipeline")


if __name__ == "__main__":
    main()
