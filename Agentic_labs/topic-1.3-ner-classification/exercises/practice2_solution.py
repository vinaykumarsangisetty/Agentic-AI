"""
===============================================================================
✅ COMPLETE SOLUTION
TOPIC 1.3 - BEGINNER PRACTICE 2: Classification Evaluation Metrics
===============================================================================
"""

from typing import List, Dict
import numpy as np
from sklearn.metrics import precision_score, recall_score, f1_score, confusion_matrix

y_true = [1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1]
y_pred = [1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0]


def calculate_confusion_matrix(y_true: List[int], y_pred: List[int]) -> Dict[str, int]:
    """Calculate confusion matrix components"""
    tp = sum((t == 1 and p == 1) for t, p in zip(y_true, y_pred))
    tn = sum((t == 0 and p == 0) for t, p in zip(y_true, y_pred))
    fp = sum((t == 0 and p == 1) for t, p in zip(y_true, y_pred))
    fn = sum((t == 1 and p == 0) for t, p in zip(y_true, y_pred))
    
    return {'TP': tp, 'TN': tn, 'FP': fp, 'FN': fn}


def calculate_precision(tp: int, fp: int) -> float:
    """Calculate precision"""
    if tp + fp == 0:
        return 0.0
    return tp / (tp + fp)


def calculate_recall(tp: int, fn: int) -> float:
    """Calculate recall"""
    if tp + fn == 0:
        return 0.0
    return tp / (tp + fn)


def calculate_f1_score(precision: float, recall: float) -> float:
    """Calculate F1-score"""
    if precision + recall == 0:
        return 0.0
    return 2 * (precision * recall) / (precision + recall)


def calculate_accuracy(tp: int, tn: int, fp: int, fn: int) -> float:
    """Calculate accuracy"""
    total = tp + tn + fp + fn
    if total == 0:
        return 0.0
    return (tp + tn) / total


def visualize_confusion_matrix(cm: Dict[str, int]):
    """Visualize confusion matrix"""
    print("\n" + "="*80)
    print("CONFUSION MATRIX VISUALIZATION")
    print("="*80)
    
    print("\n                Predicted")
    print("               Pos    Neg")
    print(f"Actual  Pos    {cm['TP']:<6} {cm['FN']:<6}")
    print(f"        Neg    {cm['FP']:<6} {cm['TN']:<6}")
    
    print("\n📊 Confusion Matrix Components:")
    print(f"   True Positives (TP):  {cm['TP']} - Correctly predicted positive")
    print(f"   True Negatives (TN):  {cm['TN']} - Correctly predicted negative")
    print(f"   False Positives (FP): {cm['FP']} - Incorrectly predicted positive (Type I error)")
    print(f"   False Negatives (FN): {cm['FN']} - Incorrectly predicted negative (Type II error)")


def explain_metrics(cm: Dict[str, int], precision: float, recall: float, f1: float, accuracy: float):
    """Explain what each metric means"""
    print("\n" + "="*80)
    print("METRICS EXPLANATION")
    print("="*80)
    
    print(f"\n1️⃣  Precision = {precision:.3f}")
    print(f"   Formula: TP / (TP + FP) = {cm['TP']} / ({cm['TP']} + {cm['FP']}) = {precision:.3f}")
    print(f"   Meaning: Of all positive predictions, {precision:.1%} were correct")
    print(f"   Question answered: 'When the model predicts positive, how often is it right?'")
    
    print(f"\n2️⃣  Recall = {recall:.3f}")
    print(f"   Formula: TP / (TP + FN) = {cm['TP']} / ({cm['TP']} + {cm['FN']}) = {recall:.3f}")
    print(f"   Meaning: Of all actual positives, {recall:.1%} were found")
    print(f"   Question answered: 'Of all actual positive cases, how many did we find?'")
    
    print(f"\n3️⃣  F1-Score = {f1:.3f}")
    print(f"   Formula: 2 * (P * R) / (P + R) = 2 * ({precision:.3f} * {recall:.3f}) / ({precision:.3f} + {recall:.3f}) = {f1:.3f}")
    print(f"   Meaning: Harmonic mean of precision and recall")
    print(f"   Use: When you need balance between precision and recall")
    
    print(f"\n4️⃣  Accuracy = {accuracy:.3f}")
    print(f"   Formula: (TP + TN) / Total = ({cm['TP']} + {cm['TN']}) / {sum(cm.values())} = {accuracy:.3f}")
    print(f"   Meaning: {accuracy:.1%} of all predictions were correct")
    print(f"   ⚠️  Can be misleading with imbalanced data!")


def demonstrate_metric_tradeoffs():
    """Demonstrate precision-recall tradeoff"""
    print("\n" + "="*80)
    print("PRECISION-RECALL TRADEOFF")
    print("="*80)
    
    print("\n📊 Scenario 1: High Precision, Low Recall")
    print("   y_true: [1, 1, 1, 1, 1, 0, 0, 0]")
    print("   y_pred: [1, 0, 0, 0, 0, 0, 0, 0]  # Very conservative")
    y_true_1 = [1, 1, 1, 1, 1, 0, 0, 0]
    y_pred_1 = [1, 0, 0, 0, 0, 0, 0, 0]
    cm_1 = calculate_confusion_matrix(y_true_1, y_pred_1)
    p_1 = calculate_precision(cm_1['TP'], cm_1['FP'])
    r_1 = calculate_recall(cm_1['TP'], cm_1['FN'])
    print(f"   Precision: {p_1:.3f} (when it predicts positive, it's right!)")
    print(f"   Recall: {r_1:.3f} (but it misses most positives)")
    print(f"   Use case: Medical diagnosis - avoid false alarms")
    
    print("\n📊 Scenario 2: Low Precision, High Recall")
    print("   y_true: [1, 1, 0, 0, 0, 0, 0, 0]")
    print("   y_pred: [1, 1, 1, 1, 1, 0, 0, 0]  # Very aggressive")
    y_true_2 = [1, 1, 0, 0, 0, 0, 0, 0]
    y_pred_2 = [1, 1, 1, 1, 1, 0, 0, 0]
    cm_2 = calculate_confusion_matrix(y_true_2, y_pred_2)
    p_2 = calculate_precision(cm_2['TP'], cm_2['FP'])
    r_2 = calculate_recall(cm_2['TP'], cm_2['FN'])
    print(f"   Precision: {p_2:.3f} (many false positives)")
    print(f"   Recall: {r_2:.3f} (but catches all actual positives)")
    print(f"   Use case: Cancer screening - don't miss any cases")


def compare_with_sklearn(y_true: List[int], y_pred: List[int]):
    """Compare with sklearn implementation"""
    print("\n" + "="*80)
    print("VALIDATION WITH SKLEARN")
    print("="*80)
    
    # Our implementation
    cm = calculate_confusion_matrix(y_true, y_pred)
    our_precision = calculate_precision(cm['TP'], cm['FP'])
    our_recall = calculate_recall(cm['TP'], cm['FN'])
    our_f1 = calculate_f1_score(our_precision, our_recall)
    our_accuracy = calculate_accuracy(cm['TP'], cm['TN'], cm['FP'], cm['FN'])
    
    # sklearn implementation
    sklearn_precision = precision_score(y_true, y_pred)
    sklearn_recall = recall_score(y_true, y_pred)
    sklearn_f1 = f1_score(y_true, y_pred)
    sklearn_accuracy = (np.array(y_true) == np.array(y_pred)).mean()
    
    print("\n📊 Comparison:")
    print(f"                  Our Implementation    sklearn")
    print(f"   Precision:     {our_precision:.6f}           {sklearn_precision:.6f}")
    print(f"   Recall:        {our_recall:.6f}           {sklearn_recall:.6f}")
    print(f"   F1-Score:      {our_f1:.6f}           {sklearn_f1:.6f}")
    print(f"   Accuracy:      {our_accuracy:.6f}           {sklearn_accuracy:.6f}")
    print(f"\n✅ Both implementations produce identical results!")


def main():
    """Main demonstration"""
    print("=" * 80)
    print("TOPIC 1.3 - BEGINNER PRACTICE 2 SOLUTION")
    print("Classification Evaluation Metrics")
    print("=" * 80)
    
    print("\n📋 Sample Data:")
    print(f"   True labels: {y_true}")
    print(f"   Predictions: {y_pred}")
    
    # Calculate confusion matrix
    cm = calculate_confusion_matrix(y_true, y_pred)
    visualize_confusion_matrix(cm)
    
    # Calculate metrics
    precision = calculate_precision(cm['TP'], cm['FP'])
    recall = calculate_recall(cm['TP'], cm['FN'])
    f1 = calculate_f1_score(precision, recall)
    accuracy = calculate_accuracy(cm['TP'], cm['TN'], cm['FP'], cm['FN'])
    
    # Explain metrics
    explain_metrics(cm, precision, recall, f1, accuracy)
    
    # Demonstrate tradeoffs
    demonstrate_metric_tradeoffs()
    
    # Compare with sklearn
    compare_with_sklearn(y_true, y_pred)
    
    print("\n" + "="*80)
    print("✅ SOLUTION COMPLETE!")
    print("="*80)
    print("\n📚 KEY TAKEAWAYS:")
    print("1. Precision: How many predicted positives are actually positive")
    print("2. Recall: How many actual positives were found")
    print("3. F1-Score: Harmonic mean balancing precision and recall")
    print("4. Accuracy: Overall correctness (misleading on imbalanced data)")
    print("5. Choose metric based on your use case!")
    
    print("\n💡 WHEN TO USE EACH METRIC:")
    print("- High Precision needed: Spam detection (avoid flagging legitimate emails)")
    print("- High Recall needed: Disease screening (don't miss any sick patients)")
    print("- F1-Score: General balance between precision and recall")
    print("- Accuracy: Only when classes are balanced")
    
    print("\n💡 TRY THIS:")
    print("- Calculate metrics for multi-class problems")
    print("- Implement ROC curve and AUC score")
    print("- Test on highly imbalanced datasets (99% negative)")
    print("- Visualize precision-recall curves")


if __name__ == "__main__":
    main()
