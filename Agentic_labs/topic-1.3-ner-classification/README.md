# Topic 1.3: NER, Text Classification, and NLP Evaluation

## 🎯 Learning Objectives

By completing these exercises, you will:
- Master Named Entity Recognition (NER) techniques
- Build text classification systems from scratch
- Understand and apply NLP evaluation metrics
- Compare rule-based, ML-based, and LLM-based approaches
- Perform systematic error analysis

## 📖 Concept Overview

### Named Entity Recognition (NER)
Identifying and classifying named entities in text:
- **Person (PER)**: "Barack Obama", "Marie Curie"
- **Organization (ORG)**: "Microsoft", "United Nations"
- **Location (LOC)**: "Paris", "Mount Everest"
- **Date (DATE)**: "January 1, 2024", "last Friday"
- **Money (MONEY)**: "$100", "50 euros"

### NER Approaches
1. **Rule-based**: Regex patterns, gazetteers
   - Fast, interpretable, domain-specific
   - Limited coverage, maintenance overhead

2. **ML-based**: CRF, spaCy models
   - Better generalization, pre-trained
   - Requires labeled data for fine-tuning

3. **LLM-based**: GPT-4, few-shot prompting
   - Flexible, handles custom entities
   - Slower, more expensive, non-deterministic

### Text Classification
Assigning predefined categories to text:
- **Binary**: Spam detection, sentiment (positive/negative)
- **Multi-class**: News categorization, intent classification
- **Multi-label**: Tag prediction, topic assignment

### Evaluation Metrics

#### Classification Metrics
- **Accuracy**: (TP + TN) / (TP + TN + FP + FN)
- **Precision**: TP / (TP + FP) — Of predicted positives, how many correct?
- **Recall**: TP / (TP + FN) — Of actual positives, how many found?
- **F1 Score**: 2 × (Precision × Recall) / (Precision + Recall) — Harmonic mean

#### NER Metrics
- **Exact match**: Entity boundaries and type must match exactly
- **Partial match**: Allows boundary overlap
- **Type accuracy**: Correct type given correct boundary

#### Generation Metrics
- **BLEU**: N-gram overlap (machine translation)
- **ROUGE**: Recall-oriented summarization
- **Perplexity**: Language model quality

## 🏋️ Exercise Structure

### Beginner Level
- **Demo**: Rule-based NER with regex
- **Practice 1**: Sentiment analysis pipeline
- **Practice 2**: Evaluation metrics from scratch

### Intermediate Level
- **Demo**: ML-based NER with spaCy
- **Practice 1**: Multi-class classification comparison
- **Practice 2**: Error analysis workshop

### Advanced Level
- **Demo**: LLM-based NER with Azure OpenAI
- **Practice 1**: BERT fine-tuning
- **Practice 2**: Comprehensive evaluation suite

## 💻 Required Libraries

```python
import spacy
import re
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from transformers import BertTokenizer, BertForSequenceClassification
from openai import AzureOpenAI
```

## 🎓 Key Takeaways

1. **NER requires understanding context** - "Apple" company vs fruit
2. **Evaluation metric choice matters** - Precision vs recall trade-off
3. **Error analysis is crucial** - Metrics alone don't show failure modes
4. **LLMs enable flexible NER** - Define custom entities via prompts
5. **F1 score balances precision/recall** - Use when classes are imbalanced

## 🔗 Connection to Later Modules

- **Module 4**: Entity extraction in RAG systems
- **Module 6**: Evaluation frameworks for GenAI
- **Production**: Monitoring classification performance
