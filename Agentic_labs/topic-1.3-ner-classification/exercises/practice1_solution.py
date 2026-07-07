"""
===============================================================================
✅ COMPLETE SOLUTION
TOPIC 1.3 - BEGINNER PRACTICE 1: Sentiment Analysis with Machine Learning
===============================================================================
"""

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from typing import List, Tuple
import numpy as np

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
    """Preprocess text"""
    return text.lower()


def create_dataset() -> Tuple[List[str], List[int]]:
    """Create dataset from reviews"""
    texts = positive_reviews + negative_reviews
    labels = [1] * len(positive_reviews) + [0] * len(negative_reviews)
    return texts, labels


def train_sentiment_classifier(X_train, y_train):
    """Train sentiment classifier"""
    # Create and fit vectorizer
    vectorizer = CountVectorizer()
    X_train_vec = vectorizer.fit_transform(X_train)
    
    # Train classifier
    classifier = MultinomialNB()
    classifier.fit(X_train_vec, y_train)
    
    return vectorizer, classifier


def predict_sentiment(text: str, vectorizer, classifier) -> Tuple[int, float]:
    """Predict sentiment for text"""
    text_vec = vectorizer.transform([preprocess_text(text)])
    prediction = classifier.predict(text_vec)[0]
    probability = classifier.predict_proba(text_vec)[0]
    confidence = probability[prediction]
    return prediction, confidence


def analyze_important_words(vectorizer, classifier, top_n=10):
    """Analyze most important words for each class"""
    feature_names = vectorizer.get_feature_names_out()
    
    # Get log probabilities for each word
    log_probs = classifier.feature_log_prob_
    
    print("\n" + "="*80)
    print("MOST IMPORTANT WORDS")
    print("="*80)
    
    # Negative words (class 0)
    neg_indices = np.argsort(log_probs[0])[-top_n:]
    print(f"\n📉 Top {top_n} words for NEGATIVE sentiment:")
    for idx in reversed(neg_indices):
        print(f"   - {feature_names[idx]} (score: {log_probs[0][idx]:.3f})")
    
    # Positive words (class 1)
    pos_indices = np.argsort(log_probs[1])[-top_n:]
    print(f"\n📈 Top {top_n} words for POSITIVE sentiment:")
    for idx in reversed(pos_indices):
        print(f"   - {feature_names[idx]} (score: {log_probs[1][idx]:.3f})")


def main():
    """Main demonstration"""
    print("=" * 80)
    print("TOPIC 1.3 - BEGINNER PRACTICE 1 SOLUTION")
    print("Sentiment Analysis with Machine Learning")
    print("=" * 80)
    
    # Create dataset
    print("\n📚 Creating dataset...")
    texts, labels = create_dataset()
    print(f"   Total samples: {len(texts)}")
    print(f"   Positive: {sum(labels)}")
    print(f"   Negative: {len(labels) - sum(labels)}")
    
    # Split data
    print("\n✂️  Splitting into train/test...")
    X_train, X_test, y_train, y_test = train_test_split(
        texts, labels, test_size=0.25, random_state=42
    )
    print(f"   Training: {len(X_train)} samples")
    print(f"   Testing: {len(X_test)} samples")
    
    # Train classifier
    print("\n🎓 Training Naive Bayes classifier...")
    vectorizer, classifier = train_sentiment_classifier(X_train, y_train)
    print(f"   Vocabulary size: {len(vectorizer.get_feature_names_out())}")
    print("   ✅ Training complete!")
    
    # Evaluate on training data
    X_train_vec = vectorizer.transform(X_train)
    train_predictions = classifier.predict(X_train_vec)
    train_accuracy = accuracy_score(y_train, train_predictions)
    
    # Evaluate on test data
    X_test_vec = vectorizer.transform(X_test)
    test_predictions = classifier.predict(X_test_vec)
    test_accuracy = accuracy_score(y_test, test_predictions)
    
    print("\n" + "="*80)
    print("EVALUATION RESULTS")
    print("="*80)
    
    print(f"\n📊 Accuracy Scores:")
    print(f"   Training Accuracy: {train_accuracy:.2%}")
    print(f"   Test Accuracy: {test_accuracy:.2%}")
    
    print(f"\n📋 Classification Report (Test Set):")
    print(classification_report(y_test, test_predictions, 
                                target_names=['Negative', 'Positive']))
    
    # Analyze important words
    analyze_important_words(vectorizer, classifier)
    
    # Test on new examples
    print("\n" + "="*80)
    print("TESTING ON NEW EXAMPLES")
    print("="*80)
    
    test_texts = [
        "This movie is absolutely amazing and wonderful",
        "I hated every second of this terrible film",
        "It was okay, nothing special",
        "Brilliant performances and great story",
        "Waste of time, very disappointing"
    ]
    
    for text in test_texts:
        prediction, confidence = predict_sentiment(text, vectorizer, classifier)
        sentiment = "POSITIVE" if prediction == 1 else "NEGATIVE"
        print(f"\n📝 Text: '{text}'")
        print(f"   Sentiment: {sentiment} (confidence: {confidence:.2%})")
    
    print("\n" + "="*80)
    print("✅ SOLUTION COMPLETE!")
    print("="*80)
    print("\n📚 KEY TAKEAWAYS:")
    print("1. Sentiment analysis is binary classification (positive/negative)")
    print("2. Bag of Words with Naive Bayes is simple but effective")
    print("3. CountVectorizer converts text to numerical features")
    print("4. Naive Bayes assumes feature independence (words)")
    print("5. Works well for small datasets and simple tasks")
    
    print("\n💡 TRY THIS:")
    print("- Use TF-IDF instead of CountVectorizer")
    print("- Try other classifiers (Logistic Regression, SVM)")
    print("- Add more training data for better accuracy")
    print("- Test on real movie reviews from IMDB dataset")
    print("- Build a 3-class classifier (positive/negative/neutral)")


if __name__ == "__main__":
    main()
