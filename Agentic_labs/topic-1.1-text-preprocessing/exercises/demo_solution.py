"""
===============================================================================
✅ COMPLETE SOLUTION
TOPIC 1.1 - BEGINNER DEMO: Basic Text Preprocessing Pipeline
===============================================================================

This file contains the full working implementation.
Try completing the exercise file first before looking at this!

🎯 What You Learned:
- Text preprocessing removes noise and normalizes text
- Each step has a specific purpose and order matters
- Preprocessing is essential for NLP tasks
"""

import re
import string
from typing import List

# Sample texts for demonstration
sample_texts = [
    """
    The Quick BROWN fox jumps over the lazy dog! 
    Visit https://example.com for more info.
    Email me at contact@example.com. #NLP #AI
    """,
    "Check out http://test.org and email test@test.com!",
    "   Multiple    spaces   and\nnewlines\n\nshould be handled!!!   "
]

# Common English stopwords
STOPWORDS = {'the', 'is', 'at', 'which', 'on', 'a', 'an', 'for', 'over', 'me', 
             'of', 'and', 'to', 'in', 'this', 'out'}


def remove_urls(text: str) -> str:
    """Remove URLs from text"""
    # Pattern matches URLs starting with http:// or https://
    pattern = r'https?://\S+'
    return re.sub(pattern, '', text)


def remove_emails(text: str) -> str:
    """Remove email addresses from text"""
    # Pattern matches standard email format
    pattern = r'\S+@\S+'
    return re.sub(pattern, '', text)


def remove_punctuation(text: str) -> str:
    """Remove punctuation from text"""
    # Create translation table that removes all punctuation
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)


def normalize_whitespace(text: str) -> str:
    """Normalize multiple spaces, tabs, newlines to single space"""
    # Replace one or more whitespace characters with single space
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def remove_stopwords(words: List[str], stopwords: set = STOPWORDS) -> List[str]:
    """Remove stopwords from list of words"""
    return [word for word in words if word.lower() not in stopwords]


def preprocess_text(text: str, remove_stops: bool = True) -> str:
    """
    Complete preprocessing pipeline combining all steps
    """
    # Step 1: Remove URLs
    text = remove_urls(text)
    
    # Step 2: Remove emails
    text = remove_emails(text)
    
    # Step 3: Convert to lowercase
    text = text.lower()
    
    # Step 4: Remove punctuation
    text = remove_punctuation(text)
    
    # Step 5: Normalize whitespace
    text = normalize_whitespace(text)
    
    # Step 6: Remove stopwords (optional)
    if remove_stops:
        words = text.split()
        words = remove_stopwords(words)
        text = ' '.join(words)
    
    return text


def demonstrate_steps(text: str):
    """Show impact of each preprocessing step"""
    print(f"📄 Original:\n{repr(text)}\n")
    
    step1 = remove_urls(text)
    print(f"1️⃣  After removing URLs:\n{repr(step1)}\n")
    
    step2 = remove_emails(step1)
    print(f"2️⃣  After removing emails:\n{repr(step2)}\n")
    
    step3 = step2.lower()
    print(f"3️⃣  After lowercasing:\n{repr(step3)}\n")
    
    step4 = remove_punctuation(step3)
    print(f"4️⃣  After removing punctuation:\n{repr(step4)}\n")
    
    step5 = normalize_whitespace(step4)
    print(f"5️⃣  After normalizing whitespace:\n{repr(step5)}\n")
    
    words = step5.split()
    step6 = remove_stopwords(words)
    final = ' '.join(step6)
    print(f"6️⃣  After removing stopwords:\n{repr(final)}\n")
    
    print(f"✅ Final: {final}")
    print(f"📊 Words: {len(text.split())} → {len(final.split())} (reduced by {len(text.split()) - len(final.split())})\n")


def main():
    """Main demonstration"""
    print("=" * 80)
    print("TOPIC 1.1 - BEGINNER DEMO SOLUTION")
    print("Basic Text Preprocessing Pipeline")
    print("=" * 80)
    print()
    
    # Demo 1: Step-by-step preprocessing
    print("=" * 80)
    print("DEMO 1: STEP-BY-STEP PREPROCESSING")
    print("=" * 80)
    print()
    demonstrate_steps(sample_texts[0])
    
    # Demo 2: Process multiple texts
    print("=" * 80)
    print("DEMO 2: PROCESSING MULTIPLE TEXTS")
    print("=" * 80)
    print()
    
    for i, text in enumerate(sample_texts, 1):
        original = text.strip()[:60] + "..." if len(text.strip()) > 60 else text.strip()
        preprocessed = preprocess_text(text)
        print(f"Text {i}:")
        print(f"  Original: {original}")
        print(f"  Preprocessed: {preprocessed}")
        print()
    
    # Demo 3: With/without stopword removal
    print("=" * 80)
    print("DEMO 3: IMPACT OF STOPWORD REMOVAL")
    print("=" * 80)
    print()
    
    test_text = "The quick brown fox jumps over the lazy dog"
    print(f"Original: {test_text}")
    print(f"Without stopwords: {preprocess_text(test_text, remove_stops=False)}")
    print(f"With stopwords: {preprocess_text(test_text, remove_stops=True)}")
    
    # Demo 4: Statistics
    print("\n" + "=" * 80)
    print("DEMO 4: PREPROCESSING STATISTICS")
    print("=" * 80)
    print()
    
    for i, text in enumerate(sample_texts, 1):
        original_words = len(text.split())
        preprocessed = preprocess_text(text)
        final_words = len(preprocessed.split()) if preprocessed else 0
        reduction_pct = ((original_words - final_words) / original_words * 100) if original_words > 0 else 0
        
        print(f"Text {i}: {original_words} → {final_words} words ({reduction_pct:.1f}% reduction)")
    
    print("\n" + "=" * 80)
    print("✅ SOLUTION COMPLETE!")
    print("=" * 80)
    print("\n📚 KEY TAKEAWAYS:")
    print("1. Text preprocessing removes noise (URLs, emails, punctuation)")
    print("2. Lowercasing normalizes text (Brown = brown)")
    print("3. Stopword removal reduces dimensionality")
    print("4. Order of operations matters!")
    print("5. Choose preprocessing steps based on your task")
    print("\n💡 TRY THIS:")
    print("- Modify STOPWORDS with domain-specific words")
    print("- Add preprocessing for numbers: re.sub(r'\\d+', '', text)")
    print("- Test on your own text data")
    print("- Try different preprocessing orders and compare results")


if __name__ == "__main__":
    main()
