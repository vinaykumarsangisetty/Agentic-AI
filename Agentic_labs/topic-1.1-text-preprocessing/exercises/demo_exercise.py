"""
===============================================================================
TOPIC 1.1 - BEGINNER DEMO: Basic Text Preprocessing Pipeline
===============================================================================

🎯 LEARNING GOALS
-----------------
By completing this exercise, you will:
1. Understand the importance of text preprocessing
2. Apply lowercasing, punctuation removal, and stopword removal
3. See the impact of each preprocessing step on text
4. Build a reusable preprocessing function

📚 KEY CONCEPTS
---------------
Text cleaning, tokenization, stopword removal, regex patterns

⏱️ TIME ESTIMATE: 30-45 minutes

🔧 VS CODE SETUP INSTRUCTIONS
------------------------------
1. Open this file in VS Code
2. Open integrated terminal: View → Terminal (or Ctrl+`)
3. Navigate to this directory:
   cd e:/ey-ai/nlp-labs/topic-1.1-text-preprocessing/beginner
4. Run this file:
   python demo_exercise.py
5. To debug:
   - Set breakpoints (click left margin or press F9)
   - Press F5 to start debugging

📝 WHAT YOU NEED TO DO
----------------------
Complete the following functions marked with # TODO:

TODO 1: Implement remove_urls() to remove http:// and https:// URLs
        Hint: Use regex pattern r'https?://\S+'
        
TODO 2: Implement remove_emails() to remove email addresses
        Hint: Use regex pattern r'\S+@\S+'
        
TODO 3: Implement remove_punctuation() to remove all punctuation
        Hint: Use string.punctuation and str.translate()
        
TODO 4: Implement remove_stopwords() to filter out common words
        Hint: Use list comprehension to filter words not in stopwords set
        
TODO 5: Implement preprocess_text() to chain all steps together
        Hint: Call functions in this order: URLs → emails → lowercase → 
              punctuation → whitespace → stopwords

💡 EXPECTED OUTPUT
------------------
When complete, you should see:
- Original text with URLs, emails, punctuation
- Step-by-step transformation showing each preprocessing stage
- Final cleaned text
- Word count statistics (before vs after)

Let's get started! 🚀
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
    """
    Remove URLs from text
    
    Args:
        text: Input text
    
    Returns:
        Text with URLs removed
    """
    # TODO: Implement this function
    # Hint: Use re.sub(r'https?://\S+', '', text)
    pattern = r'https?://\S+'
    return re.sub(pattern, '', text)


def remove_emails(text: str) -> str:
    """
    Remove email addresses from text
    
    Args:
        text: Input text
    
    Returns:
        Text with emails removed
    """
    # TODO: Implement this function
    pattern = r'\S+@\S+'
    return re.sub(pattern, '', text)


def remove_punctuation(text: str) -> str:
    """
    Remove punctuation from text
    
    Args:
        text: Input text
    
    Returns:
        Text with punctuation removed
    """
    # TODO: Implement this function
    # Hint: Use str.translate() with string.punctuation
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)


def normalize_whitespace(text: str) -> str:
    """
    Normalize multiple spaces, tabs, newlines to single space
    
    Args:
        text: Input text
    
    Returns:
        Text with normalized whitespace
    """
    # This one is done for you as an example!
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def remove_stopwords(words: List[str], stopwords: set = STOPWORDS) -> List[str]:
    """
    Remove stopwords from list of words
    
    Args:
        words: List of words
        stopwords: Set of stopwords to remove
    
    Returns:
        List of words with stopwords removed
    """
    # TODO: Implement this function
    # Hint: return [word for word in words if word.lower() not in stopwords]
    return [word for word in words if word.lower() not in stopwords]


def preprocess_text(text: str, remove_stops: bool = True) -> str:
    """
    Complete preprocessing pipeline combining all steps
    
    Args:
        text: Input text to preprocess
        remove_stops: Whether to remove stopwords (default True)
    
    Returns:
        Preprocessed text as string
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


def main():
    """
    Main execution function
    """
    print("=" * 80)
    print("TOPIC 1.1 - BEGINNER DEMO")
    print("Basic Text Preprocessing Pipeline")
    print("=" * 80)
    print()
    
    # Test your implementations here
    test_text = sample_texts[0]
    print(f"Original text:\n{test_text}\n")
    
    # TODO: Call your functions and print results
    # Example:
    # preprocessed = preprocess_text(test_text)
    # print(f"Preprocessed: {preprocessed}")
    
    print("\n⚠️  Complete the TODO items above, then run this file again!")
    print("Compare your output with demo_solution.py when done.")


if __name__ == "__main__":
    main()
