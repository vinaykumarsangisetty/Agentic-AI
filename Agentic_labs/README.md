# NLP Fundamentals - Hands-On Lab Exercises

Comprehensive hands-on exercises for learning NLP fundamentals through coding. Designed for VS Code with Azure OpenAI integration.

## 📁 Repository Structure

```
nlp-labs/
├── instructor-demos/              ← For instructors: Live demo scripts
│   ├── README.md
│   ├── demo-1.1-text-preprocessing.py
│   ├── demo-1.2-semantic-similarity.py
│   ├── demo-1.3-ner-classification.py
│   └── demo-1.4-rag-genai.py
│
├── topic-1.1-text-preprocessing/
│   ├── README.md
│   └── exercises/
│       ├── demo_exercise.py & demo_solution.py
│       ├── practice1_exercise.py & practice1_solution.py
│       └── practice2_exercise.py & practice2_solution.py
│
├── topic-1.2-semantic-similarity/
├── topic-1.3-ner-classification/
└── topic-1.4-rag/
```

### For Students
Each topic contains:
- **README.md**: Concept overview and learning objectives
- **exercises/**: Hands-on coding exercises with solutions

Each exercise includes:
- `*_exercise.py`: Starter code with step-by-step TODOs and hints
- `*_solution.py`: Complete working solution with explanations

### For Instructors
- **instructor-demos/**: Professional demo scripts for live classroom instruction
- Detailed teaching notes and discussion questions
- Interactive sections with pause points
- Real-world examples and applications

## 📚 Topics

### [Topic 1.1: Text Preprocessing](./topic-1.1-text-preprocessing/)
**Concepts:** Tokenization, stopwords, Bag of Words  
**Exercises:** Basic preprocessing pipeline, tokenization strategies, BoW implementation

### [Topic 1.2: Semantic Similarity](./topic-1.2-semantic-similarity/)
**Concepts:** Cosine similarity, inverted index, BM25  
**Exercises:** Similarity from scratch, building search index, ranking algorithms

### [Topic 1.3: NER & Classification](./topic-1.3-ner-classification/)
**Concepts:** Named entity recognition, sentiment analysis, evaluation metrics  
**Exercises:** Rule-based NER, text classification, precision/recall/F1

### [Topic 1.4: RAG & GenAI](./topic-1.4-rag/)
**Concepts:** Retrieval-Augmented Generation, embeddings, LLM integration  
**Exercises:** End-to-end pipeline, embedding comparison, RAG with Azure OpenAI

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd nlp-labs
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Azure OpenAI (Optional)

Some exercises use Azure OpenAI. Create a `.env` file in the root directory:

```env
AZURE_OPENAI_ENDPOINT=your-endpoint-here
AZURE_OPENAI_API_KEY=your-api-key-here
AZURE_OPENAI_DEPLOYMENT_NAME=your-deployment-name
AZURE_OPENAI_EMBEDDING_DEPLOYMENT=text-embedding-ada-002
```

### 4. Run Your First Exercise

```bash
cd topic-1.1-text-preprocessing/exercises
python demo_solution.py
```

## 📖 How to Use These Labs

### For Students

1. **Read the topic README** to understand concepts
2. **Open the exercise file** (`*_exercise.py`) in VS Code
3. **Follow the TODO instructions** with step-by-step hints
4. **Run and test your code** frequently
5. **Compare with solution** (`*_solution.py`) when complete

### Each Exercise Includes

- 🎯 **Learning Goals**: Clear objectives
- 📝 **TODO Instructions**: Step-by-step guidance with hints
- 🔧 **VS Code Setup**: How to run and debug
- 💡 **Expected Output**: What success looks like
- ✅ **Complete Solution**: Working code with explanations
- 📚 **Key Takeaways**: Learning points

## 💻 Example Exercise Structure

```python
"""
🎯 LEARNING GOALS
1. Understand text preprocessing importance
2. Implement basic cleaning functions
3. Build reusable pipeline

📝 WHAT YOU NEED TO DO
TODO 1: Implement remove_urls()
        Hint: Use re.sub(r'https?://\S+', '', text)

💡 EXPECTED OUTPUT
- Cleaned text without URLs
- Before/after comparison
"""
```

## 🎓 Learning Path

**Recommended Order:**
1. Topic 1.1 → Text Preprocessing
2. Topic 1.2 → Semantic Similarity  
3. Topic 1.3 → NER & Classification
4. Topic 1.4 → RAG & GenAI

**For Each Topic:**
- Start with `demo_exercise.py` to learn core concepts
- Practice with `practice1_exercise.py` and `practice2_exercise.py`
- Compare your implementation with solution files

## 🔧 Requirements

- Python 3.8+
- VS Code (recommended)
- Azure OpenAI access (for Topic 1.4 exercises)

## 📦 Key Libraries

- **nltk**: Tokenization, stopwords, stemming
- **scikit-learn**: TF-IDF, classification, metrics
- **numpy/pandas**: Data manipulation
- **openai**: Azure OpenAI integration (Topic 1.4)

## 👨‍🏫 For Instructors

### Live Demo Scripts
The [instructor-demos/](./instructor-demos/) folder contains professional demo scripts for classroom instruction:

- **demo-1.1-text-preprocessing.py** (20-25 min) - Text cleaning and pipelines
- **demo-1.2-semantic-similarity.py** (25-30 min) - Cosine similarity and search
- **demo-1.3-ner-classification.py** (25-30 min) - Entity extraction and classification
- **demo-1.4-rag-genai.py** (30-35 min) - RAG with Azure OpenAI

Each demo includes:
- 📋 Detailed teaching notes
- 🎯 Learning objectives
- ⏸️ Interactive pause points
- ❓ Discussion questions
- 💡 Real-world examples
- ✅ Key takeaways

**Usage**: Run these scripts during live lectures to demonstrate concepts before students work on exercises.

**See**: [instructor-demos/README.md](./instructor-demos/README.md) for complete teaching guide.

## 🆘 Getting Help

### For Students
- **Stuck on an exercise?** Check the hints in TODO comments
- **Code not working?** Compare with the solution file
- **Concept unclear?** Read the topic README for explanations
- **Need more examples?** Run the solution files to see working demos

### For Instructors
- **Need demo materials?** Check the `instructor-demos/` folder
- **Teaching strategies?** Review teaching notes in demo scripts
- **Technical setup?** See QUICK_START.md for configuration
