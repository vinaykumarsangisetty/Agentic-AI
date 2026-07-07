"""
===============================================================================
✅ COMPLETE SOLUTION
TOPIC 1.1 - BEGINNER PRACTICE 1: Tokenization Strategies
===============================================================================

This file contains the full working implementation.
Try completing the exercise file first!
"""

import re
import nltk
from typing import List
from collections import Counter

# Download NLTK data (only needs to run once)
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt', quiet=True)

# Sample texts demonstrating different tokenization challenges
sample_texts = [
    "Hello, world! How are you today?",
    "It's a beautiful day. Don't you think?",
    "Email: test@example.com, URL: https://test.com",
    "Prices: $19.99, €25.50, £15.00",
    "I'm really excited!!! This is amazing!!!!"
]


def character_tokenize(text: str) -> List[str]:
    """Split text into individual characters"""
    return list(text)


def word_tokenize_simple(text: str) -> List[str]:
    """Split text by whitespace (simplest method)"""
    return text.split()


def word_tokenize_punctuation(text: str) -> List[str]:
    """Split text into words and punctuation tokens"""
    # This pattern matches either words (\w+) or punctuation ([^\w\s])
    return re.findall(r'\w+|[^\w\s]', text)


def word_tokenize_nltk(text: str) -> List[str]:
    """Use NLTK's word tokenizer (handles contractions well)"""
    return nltk.word_tokenize(text)


def compare_tokenizers(text: str):
    """Compare all tokenization methods"""
    print(f"\n{'='*70}")
    print(f"Text: {text}")
    print(f"{'='*70}")
    
    # Get tokens from each method
    char_tokens = character_tokenize(text)
    simple_tokens = word_tokenize_simple(text)
    punct_tokens = word_tokenize_punctuation(text)
    nltk_tokens = word_tokenize_nltk(text)
    
    # Display results
    print(f"\n1️⃣  Character: {len(char_tokens)} tokens")
    print(f"   First 20: {char_tokens[:20]}")
    
    print(f"\n2️⃣  Simple (whitespace): {len(simple_tokens)} tokens")
    print(f"   Tokens: {simple_tokens}")
    
    print(f"\n3️⃣  With punctuation: {len(punct_tokens)} tokens")
    print(f"   Tokens: {punct_tokens}")
    
    print(f"\n4️⃣  NLTK: {len(nltk_tokens)} tokens")
    print(f"   Tokens: {nltk_tokens}")
    
    # Analysis
    print(f"\n📊 Comparison:")
    print(f"   Character tokenization: Good for character-level models")
    print(f"   Simple tokenization: Fast but keeps punctuation with words")
    print(f"   Punct tokenization: Separates punctuation, good for most tasks")
    print(f"   NLTK tokenization: Handles contractions best (It's → It, 's)")


def analyze_tokenization_differences():
    """Analyze differences between tokenization methods"""
    print("\n" + "="*80)
    print("DETAILED ANALYSIS: When Each Method Works Best")
    print("="*80)
    
    # Test case 1: Contractions
    text1 = "It's a beautiful day. Don't you think?"
    print(f"\n📝 Test 1 - Contractions: {text1}")
    print(f"Simple: {word_tokenize_simple(text1)}")
    print(f"→ Problem: Keeps apostrophes attached")
    print(f"NLTK: {word_tokenize_nltk(text1)}")
    print(f"→ Better: Splits contractions properly")
    
    # Test case 2: URLs and emails
    text2 = "Visit https://example.com"
    print(f"\n📝 Test 2 - URLs: {text2}")
    print(f"Simple: {word_tokenize_simple(text2)}")
    print(f"→ Keeps URL as one token (might want this!)")
    print(f"Punct: {word_tokenize_punctuation(text2)}")
    print(f"→ Splits URL into parts (usually not desired)")
    
    # Test case 3: Punctuation
    text3 = "Hello, world! How are you?"
    print(f"\n📝 Test 3 - Punctuation: {text3}")
    print(f"Simple: {word_tokenize_simple(text3)}")
    print(f"→ Punctuation attached to words")
    print(f"Punct: {word_tokenize_punctuation(text3)}")
    print(f"→ Punctuation separated")
    print(f"NLTK: {word_tokenize_nltk(text3)}")
    print(f"→ Punctuation separated, smart handling")


def main():
    """Main demonstration"""
    print("=" * 80)
    print("TOPIC 1.1 - BEGINNER PRACTICE 1 SOLUTION")
    print("Tokenization Strategies Comparison")
    print("=" * 80)
    
    # Demo 1: Compare all methods on each sample text
    print("\n" + "="*80)
    print("DEMO 1: COMPARING ALL TOKENIZATION METHODS")
    print("="*80)
    
    for text in sample_texts:
        compare_tokenizers(text)
    
    # Demo 2: Detailed analysis
    print("\n" + "="*80)
    print("DEMO 2: DETAILED ANALYSIS")
    print("="*80)
    analyze_tokenization_differences()
    
    # Demo 3: Statistics
    print("\n" + "="*80)
    print("DEMO 3: TOKENIZATION STATISTICS")
    print("="*80)
    
    for i, text in enumerate(sample_texts, 1):
        print(f"\nText {i}: {text}")
        print(f"  Char tokens: {len(character_tokenize(text))}")
        print(f"  Simple tokens: {len(word_tokenize_simple(text))}")
        print(f"  Punct tokens: {len(word_tokenize_punctuation(text))}")
        print(f"  NLTK tokens: {len(word_tokenize_nltk(text))}")
    
    print("\n" + "="*80)
    print("✅ SOLUTION COMPLETE!")
    print("="*80)
    print("\n📚 KEY TAKEAWAYS:")
    print("1. Character tokenization: Best for character-level models (RNNs)")
    print("2. Simple tokenization: Fast but crude, keeps punctuation")
    print("3. Punct tokenization: Good balance, separates punctuation")
    print("4. NLTK tokenization: Most sophisticated, handles edge cases")
    print("5. Choice depends on your task and language!")
    
    print("\n🎯 WHEN TO USE EACH:")
    print("- Character: Character-level language models, byte-pair encoding")
    print("- Simple: Quick prototyping, informal text")
    print("- Punct: General NLP tasks, feature extraction")
    print("- NLTK: Production systems, research, multiple languages")
    
    print("\n💡 TRY THIS:")
    print("- Test on text in your domain (medical, legal, social media)")
    print("- Try other languages (NLTK supports many!)")
    print("- Implement your own tokenizer with custom rules")
    print("- Compare speed: Simple >> Punct > NLTK")


if __name__ == "__main__":
    main()
