"""
===============================================================================
✅ COMPLETE SOLUTION
TOPIC 1.4 - BEGINNER PRACTICE 2: Simple RAG System
===============================================================================
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from typing import List, Dict, Tuple
import numpy as np

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
        """Initialize RAG system"""
        self.documents = documents
        self.texts = [doc['text'] for doc in documents]
        
        # Create and fit vectorizer
        self.vectorizer = TfidfVectorizer()
        self.doc_vectors = self.vectorizer.fit_transform(self.texts)
        
        print(f"📚 Initialized RAG with {len(documents)} documents")
        print(f"   Vocabulary size: {len(self.vectorizer.vocabulary_)}")
    
    def retrieve(self, query: str, top_k: int = 2) -> List[Tuple[Dict, float]]:
        """Retrieve most relevant documents"""
        # Transform query
        query_vector = self.vectorizer.transform([query])
        
        # Compute similarities
        similarities = cosine_similarity(query_vector, self.doc_vectors)[0]
        
        # Get top k indices
        top_indices = np.argsort(similarities)[-top_k:][::-1]
        
        # Return documents with scores
        results = [
            (self.documents[idx], similarities[idx])
            for idx in top_indices
        ]
        
        return results
    
    def generate_answer(self, query: str, retrieved_docs: List[Tuple[Dict, float]]) -> str:
        """Generate answer using retrieved context"""
        if not retrieved_docs:
            return "No relevant information found."
        
        # Build context from retrieved documents
        context_parts = []
        for doc, score in retrieved_docs:
            context_parts.append(f"- {doc['text']}")
        
        context = "\n".join(context_parts)
        
        # Simple template-based generation
        answer = f"Based on the retrieved information:\n\n{context}\n\n"
        answer += f"In summary: The most relevant information about '{query}' "
        answer += f"can be found in the context above."
        
        return answer
    
    def query(self, question: str, top_k: int = 2) -> Dict:
        """Complete RAG query"""
        # Retrieve
        retrieved = self.retrieve(question, top_k)
        
        # Generate
        answer = self.generate_answer(question, retrieved)
        
        return {
            'question': question,
            'retrieved_docs': retrieved,
            'answer': answer
        }


def demonstrate_rag_workflow(rag: SimpleRAG, query: str):
    """Demonstrate complete RAG workflow"""
    print(f"\n🔍 Query: '{query}'")
    print("="*80)
    
    # Step 1: Retrieval
    print("\n📖 Step 1: RETRIEVAL")
    retrieved = rag.retrieve(query, top_k=2)
    
    for rank, (doc, score) in enumerate(retrieved, 1):
        print(f"\n   Rank {rank} (score: {score:.3f}):")
        print(f"   Topic: {doc['topic']}")
        print(f"   Text: {doc['text']}")
    
    # Step 2: Generation
    print("\n✍️  Step 2: GENERATION")
    result = rag.query(query, top_k=2)
    print(f"\n{result['answer']}")


def compare_with_without_retrieval(rag: SimpleRAG):
    """Compare answers with and without retrieval"""
    print("\n" + "="*80)
    print("COMPARISON: With vs Without Retrieval")
    print("="*80)
    
    query = "What is Python used for?"
    
    print(f"\n❓ Question: '{query}'")
    
    # Without retrieval (baseline)
    print("\n❌ Without Retrieval (No Context):")
    print("   'I don't have specific information to answer this question.'")
    print("   Problem: Generic response, no grounding")
    
    # With retrieval
    print("\n✅ With Retrieval (RAG):")
    result = rag.query(query, top_k=1)
    retrieved_doc = result['retrieved_docs'][0][0]
    print(f"   Retrieved: '{retrieved_doc['text']}'")
    print(f"   Answer grounded in actual document content!")


def evaluate_retrieval_quality(rag: SimpleRAG):
    """Evaluate retrieval quality"""
    print("\n" + "="*80)
    print("RETRIEVAL QUALITY EVALUATION")
    print("="*80)
    
    test_queries = [
        ('What is Python?', 'Python'),
        ('Tell me about machine learning', 'ML'),
        ('How does NLP work?', 'NLP'),
        ('What is RAG?', 'RAG')
    ]
    
    correct = 0
    total = len(test_queries)
    
    print("\n📊 Test Results:")
    for query, expected_topic in test_queries:
        retrieved = rag.retrieve(query, top_k=1)
        top_doc, score = retrieved[0]
        
        is_correct = top_doc['topic'] == expected_topic
        if is_correct:
            correct += 1
        
        status = "✅" if is_correct else "❌"
        print(f"\n   {status} Query: '{query}'")
        print(f"      Expected: {expected_topic}, Got: {top_doc['topic']} (score: {score:.3f})")
    
    accuracy = correct / total
    print(f"\n📈 Retrieval Accuracy: {correct}/{total} = {accuracy:.1%}")


def explain_rag_benefits():
    """Explain RAG benefits"""
    print("\n" + "="*80)
    print("WHY USE RAG?")
    print("="*80)
    
    print("\n✅ Benefits of RAG:")
    print("   1. Grounded responses - answers based on real documents")
    print("   2. Factual accuracy - retrieves actual information")
    print("   3. Source attribution - can show which documents used")
    print("   4. Up-to-date - add new documents without retraining")
    print("   5. Reduced hallucination - generates from retrieved content")
    
    print("\n🏗️  RAG Architecture:")
    print("   Query → Retrieval (find relevant docs)")
    print("        → Augmentation (add docs as context)")
    print("        → Generation (produce answer from context)")
    
    print("\n🔄 Compared to Other Approaches:")
    print("   Pure Generation (No Retrieval):")
    print("      ❌ May hallucinate facts")
    print("      ❌ Knowledge cutoff date limitation")
    print("      ❌ Can't access private documents")
    
    print("\n   RAG (Retrieval + Generation):")
    print("      ✅ Grounded in retrieved documents")
    print("      ✅ Can access fresh/private information")
    print("      ✅ Transparent (can show sources)")
    
    print("\n   Fine-tuning:")
    print("      ❌ Expensive (requires retraining)")
    print("      ❌ Can't easily update knowledge")
    print("      ✅ Better for style/format adaptation")


def main():
    """Main demonstration"""
    print("=" * 80)
    print("TOPIC 1.4 - BEGINNER PRACTICE 2 SOLUTION")
    print("Simple RAG System")
    print("=" * 80)
    
    # Initialize RAG
    print("\n🚀 Initializing RAG System...")
    rag = SimpleRAG(knowledge_base)
    
    # Demonstrate RAG workflow
    print("\n" + "="*80)
    print("RAG WORKFLOW DEMONSTRATION")
    print("="*80)
    
    queries = [
        "What is Python?",
        "Tell me about RAG",
        "How does machine learning work?"
    ]
    
    for query in queries:
        demonstrate_rag_workflow(rag, query)
    
    # Compare with/without retrieval
    compare_with_without_retrieval(rag)
    
    # Evaluate retrieval
    evaluate_retrieval_quality(rag)
    
    # Explain benefits
    explain_rag_benefits()
    
    print("\n" + "="*80)
    print("✅ SOLUTION COMPLETE!")
    print("="*80)
    print("\n📚 KEY TAKEAWAYS:")
    print("1. RAG = Retrieval + Augmentation + Generation")
    print("2. Retrieval finds relevant documents from knowledge base")
    print("3. Augmentation adds retrieved docs as context")
    print("4. Generation produces answer grounded in context")
    print("5. RAG reduces hallucination and enables up-to-date responses")
    
    print("\n💡 PRODUCTION RAG SYSTEMS:")
    print("   Instead of TF-IDF, use:")
    print("   - Dense embeddings (BERT, Sentence-Transformers)")
    print("   - Vector databases (Pinecone, Weaviate, ChromaDB)")
    print("   - Hybrid search (dense + sparse)")
    print("   - Reranking (cross-encoder for better ranking)")
    print("   - LLMs for generation (OpenAI, Claude, Llama)")
    
    print("\n💡 TRY THIS:")
    print("- Use Azure OpenAI embeddings instead of TF-IDF")
    print("- Add more documents to knowledge base")
    print("- Implement citation (show which doc each fact came from)")
    print("- Try different top_k values (1, 3, 5)")
    print("- Build RAG with ChromaDB + GPT-4 (next level!)")


if __name__ == "__main__":
    main()
