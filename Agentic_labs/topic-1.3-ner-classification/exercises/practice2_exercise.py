"""
===============================================================================
TOPIC 1.3 - BEGINNER PRACTICE 2: Classification Evaluation Metrics
===============================================================================

🎯 LEARNING GOALS
-----------------
1. Calculate precision, recall, and F1-score from scratch
2. Create and interpret confusion matrix
3. Understand when to use each metric
4. Handle imbalanced datasets

📚 KEY CONCEPTS: Precision, recall, F1-score, confusion matrix, true positives

⏱️ TIME ESTIMATE: 45-60 minutes

🔧 VS CODE SETUP
----------------
1. Open this file in VS Code
2. Terminal: cd e:/ey-ai/nlp-labs/topic-1.3-ner-classification/beginner
3. Run: python practice2_exercise.py
4. Debug: F9 (breakpoint), F5 (start)

📝 WHAT YOU NEED TO DO
----------------------
TODO 1: Implement calculate_confusion_matrix()
        Count TP, TN, FP, FN from predictions and labels
        
TODO 2: Implement calculate_precision()
        Formula: TP / (TP + FP)
        
TODO 3: Implement calculate_recall()
        Formula: TP / (TP + FN)
        
TODO 4: Implement calculate_f1_score()
        Formula: 2 * (precision * recall) / (precision + recall)
        
TODO 5: Compare your implementation with sklearn.metrics

💡 EXPECTED OUTPUT
------------------
- Confusion matrix visualization
- Precision, recall, F1-score for each class
- Comparison with sklearn showing identical results

Let's get started! 🚀
"""

from typing import List, Tuple, Dict
import numpy as np

# Sample predictions and labels for testing
y_true = [1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1]
y_pred = [1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0]


def calculate_confusion_matrix(y_true: List[int], y_pred: List[int]) -> Dict[str, int]:
    """
    Calculate confusion matrix components
    
    Args:
        y_true: True labels
        y_pred: Predicted labels
    
    Returns:
        Dictionary with TP, TN, FP, FN
        
    Example:
        >>> calculate_confusion_matrix([1,0,1], [1,0,0])
        {'TP': 1, 'TN': 1, 'FP': 0, 'FN': 1}
    """
    # TODO: Implement confusion matrix calculation
    # Hint:
    # TP = true=1 and pred=1
    # TN = true=0 and pred=0
    # FP = true=0 and pred=1 (False Positive)
    # FN = true=1 and pred=0 (False Negative)
    pass


def calculate_precision(tp: int, fp: int) -> float:
    """
    Calculate precision
    
    Args:
        tp: True positives
        fp: False positives
    
    Returns:
        Precision score
    """
    # TODO: Implement precision formula
    # Precision = TP / (TP + FP)
    # Handle division by zero!
    pass


def calculate_recall(tp: int, fn: int) -> float:
    """
    Calculate recall
    
    Args:
        tp: True positives
        fn: False negatives
    
    Returns:
        Recall score
    """
    # TODO: Implement recall formula
    # Recall = TP / (TP + FN)
    pass


def calculate_f1_score(precision: float, recall: float) -> float:
    """
    Calculate F1-score
    
    Args:
        precision: Precision score
        recall: Recall score
    
    Returns:
        F1-score
    """
    # TODO: Implement F1-score formula
    # F1 = 2 * (precision * recall) / (precision + recall)
    pass


def calculate_accuracy(tp: int, tn: int, fp: int, fn: int) -> float:
    """
    Calculate accuracy
    
    Args:
        tp, tn, fp, fn: Confusion matrix components
    
    Returns:
        Accuracy score
    """
    # TODO: Implement accuracy formula
    # Accuracy = (TP + TN) / (TP + TN + FP + FN)
    pass


def main():
    """Main execution"""
    print("=" * 80)
    print("TOPIC 1.3 - BEGINNER PRACTICE 2")
    print("Classification Evaluation Metrics")
    print("=" * 80)
    print()
    
    # TODO: Calculate confusion matrix
    # TODO: Calculate all metrics
    # TODO: Compare with sklearn
    # TODO: Test on imbalanced dataset
    
    print("\n⚠️  Complete the TODO items above, then run this file again!")
    print("Compare your output with practice2_solution.py when done.")


if __name__ == "__main__":
    main()
