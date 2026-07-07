"""
===============================================================================
TOPIC 1.3 - BEGINNER PRACTICE 1: Sentiment Analysis with Machine Learning
===============================================================================

🎯 LEARNING GOALS
-----------------
1. Build a simple sentiment classifier
2. Use Bag of Words representation for features
3. Train and evaluate Naive Bayes classifier
4. Understand basic text classification pipeline

📚 KEY CONCEPTS: Sentiment analysis, text classification, Naive Bayes, CountVectorizer

⏱️ TIME ESTIMATE: 45-60 minutes

🔧 VS CODE SETUP
----------------
1. Open this file in VS Code
2. Terminal: cd e:/ey-ai/nlp-labs/topic-1.3-ner-classification/beginner
3. Run: python practice1_exercise.py
4. Debug: F9 (breakpoint), F5 (start)

📝 WHAT YOU NEED TO DO
----------------------
TODO 1: Preprocess text data (lowercase, remove punctuation)
        Hint: Use techniques from Topic 1.1
        
TODO 2: Create BoW features using CountVectorizer
        Hint: from sklearn.feature_extraction.text import CountVectorizer
        
TODO 3: Train Naive Bayes classifier
        Hint: from sklearn.naive_bayes import MultinomialNB
        
TODO 4: Evaluate using accuracy, precision, recall
        Hint: from sklearn.metrics import classification_report
        
TODO 5: Test on new examples

💡 EXPECTED OUTPUT
------------------
- Training and test accuracy scores
- Classification report with precision/recall/F1
- Predictions on new sample texts

Let's get started! 🚀
"""

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from typing import List, Tuple

# Sample movie reviews dataset
positive_reviews = [
    "This movie was excellent and I loved it",
    "Great film with amazing acting",
    "Wonderful story and brilliant performances",
    "I really enjoyed this movie, highly recommend",
    "Fantastic movie, one of the best I've seen",
    "Superb film with great direction",
    "Loved every minute of it, amazing experience",
    "Outstanding performances by all actors"
]

negative_reviews = [
    "This movie was terrible and boring",
    "Awful film, waste of time",
    "Poor acting and bad story",
    "I hated this movie, very disappointing",
    "Terrible film, don't watch it",
    "Boring and poorly made",
    "Worst movie I've ever seen",
    "Disappointing and badly acted"
]


def preprocess_text(text: str) -> str:
    """
    Preprocess text for classification
    
    Args:
        text: Input text
    
    Returns:
        Preprocessed text
    """
    # TODO: Implement text preprocessing
    # Hint: Lowercase and basic cleaning
    # text = text.lower()
    # Remove punctuation if needed
    pass


def create_dataset() -> Tuple[List[str], List[int]]:
    """
    Create dataset from reviews
    
    Returns:
        Tuple of (texts, labels) where labels are 0 (negative) or 1 (positive)
    """
    # TODO: Combine reviews and create labels
    # Hint: positive_reviews get label 1, negative_reviews get label 0
    pass


def train_sentiment_classifier(X_train: List[str], y_train: List[int]):
    """
    Train sentiment classifier
    
    Args:
        X_train: Training texts
        y_train: Training labels
    
    Returns:
        Tuple of (vectorizer, classifier)
    """
    # TODO: Create and train classifier
    # Hint:
    # 1. Create CountVectorizer
    # 2. Fit and transform training data
    # 3. Train MultinomialNB
    pass


def main():
    """Main execution"""
    print("=" * 80)
    print("TOPIC 1.3 - BEGINNER PRACTICE 1")
    print("Sentiment Analysis with Machine Learning")
    print("=" * 80)
    print()
    
    # TODO: Create dataset
    # TODO: Split into train/test
    # TODO: Train classifier
    # TODO: Evaluate performance
    # TODO: Test on new examples
    
    print("\n⚠️  Complete the TODO items above, then run this file again!")
    print("Compare your output with practice1_solution.py when done.")


if __name__ == "__main__":
    main()
