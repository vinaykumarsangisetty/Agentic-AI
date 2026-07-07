"""
===============================================================================
TOPIC 1.1 - BEGINNER PRACTICE 1: Tokenization Strategies
===============================================================================

🎯 LEARNING GOALS
-----------------
By completing this exercise, you will:
1. Understand different tokenization approaches
2. Implement character, word, and whitespace tokenization
3. Compare tokenization results on different text types
4. Learn when to use each tokenization strategy

📚 KEY CONCEPTS
---------------
Character tokenization, word tokenization, whitespace splitting, token boundaries

⏱️ TIME ESTIMATE: 45-60 minutes

🔧 VS CODE SETUP INSTRUCTIONS
------------------------------
1. Open this file in VS Code
2. Open integrated terminal: View → Terminal (or Ctrl+`)
3. Navigate to: cd e:/ey-ai/nlp-labs/topic-1.1-text-preprocessing/beginner
4. Run: python practice1_exercise.py
5. To debug: Set breakpoints (F9) and press F5

📝 WHAT YOU NEED TO DO
----------------------
TODO 1: Implement character_tokenize() - split text into individual characters
        Hint: Use list(text) or [char for char in text]
        
TODO 2: Implement word_tokenize_simple() - split by whitespace
        Hint: Use text.split()
        
TODO 3: Implement word_tokenize_punctuation() - handle punctuation as separate tokens
        Hint: Use regex pattern r'\w+|[^\w\s]' to match words or punctuation
        
TODO 4: Implement word_tokenize_nltk() - use NLTK's word tokenizer
        Hint: import nltk; Use nltk.word_tokenize(text)
        
TODO 5: Compare all methods and analyze differences

💡 EXPECTED OUTPUT
------------------
- Comparison table showing token counts for each method
- Side-by-side examples of how each method handles special cases
- Analysis of which method works best for different scenarios

Let's get started! 🚀
"""

import re
from typing import List
from collections import Counter

# Sample texts for testing different tokenization methods
sample_texts = [
    "Hello, world! How are you today?",
    "It's a beautiful day. Don't you think?",
    "Email: test@example.com, URL: https://test.com",
    "Prices: $19.99, €25.50, £15.00",
    "I'm really excited!!! This is amazing!!!!"
]


def character_tokenize(text: str) -> List[str]:
    """
    Split text into individual characters
    
    Args:
        text: Input text
    
    Returns:
        List of characters
        
    Example:
        >>> character_tokenize("Hi!")
        ['H', 'i', '!']
    """
    # TODO: Implement this function
    # Hint: Simply convert text to list: list(text)
    pass


def word_tokenize_simple(text: str) -> List[str]:
    """
    Split text by whitespace (simplest method)
    
    Args:
        text: Input text
    
    Returns:
        List of tokens
        
    Example:
        >>> word_tokenize_simple("Hello world")
        ['Hello', 'world']
    """
    # TODO: Implement this function
    # Hint: Use text.split()
    pass


def word_tokenize_punctuation(text: str) -> List[str]:
    """
    Split text into words and punctuation tokens
    
    Args:
        text: Input text
    
    Returns:
        List of tokens (words and punctuation separate)
        
    Example:
        >>> word_tokenize_punctuation("Hello, world!")
        ['Hello', ',', 'world', '!']
    """
    # TODO: Implement this function
    # Hint: Use re.findall(r'\w+|[^\w\s]', text)
    # This pattern matches either words (\w+) or punctuation ([^\w\s])
    pass


def word_tokenize_nltk(text: str) -> List[str]:
    """
    Use NLTK's word tokenizer (handles contractions, punctuation well)
    
    Args:
        text: Input text
    
    Returns:
        List of tokens
        
    Example:
        >>> word_tokenize_nltk("It's great!")
        ['It', "'s", 'great', '!']
    """
    # TODO: Implement this function
    # Hint: 
    # import nltk
    # nltk.download('punkt', quiet=True)  # Download tokenizer data
    # return nltk.word_tokenize(text)
    pass


def compare_tokenizers(text: str):
    """
    Compare all tokenization methods on given text
    
    Args:
        text: Input text to tokenize
    """
    # TODO: Implement this function
    # Call all tokenization methods and print results side by side
    # Show token counts and first few tokens from each method
    pass


def main():
    """Main execution"""
    print("=" * 80)
    print("TOPIC 1.1 - BEGINNER PRACTICE 1")
    print("Tokenization Strategies")
    print("=" * 80)
    print()
    
    # TODO: Test your implementations
    # Example:
    # for text in sample_texts:
    #     print(f"\nText: {text}")
    #     compare_tokenizers(text)
    
    print("\n⚠️  Complete the TODO items above, then run this file again!")
    print("Compare your output with practice1_solution.py when done.")


if __name__ == "__main__":
    main()
