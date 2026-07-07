# 🎓 NLP Fundamentals Labs - Navigation

**Hands-On Exercises for Learning NLP Through Coding**

---

## 📋 Documentation Overview

| Document | Purpose | Start Here? |
|----------|---------|-------------|
| **[README.md](README.md)** | Repository overview & setup | ✅ START HERE |
| **[QUICK_START.md](QUICK_START.md)** | 5-minute getting started guide | For quick setup |
| **[EXERCISE_CATALOG.md](EXERCISE_CATALOG.md)** | Complete exercise listing | For planning |
| **This File** | Navigation & learning paths | Reference |

---

## 🎯 Getting Started

### For Students

**Day 1: Setup** (15 minutes)
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Configure Azure OpenAI (optional): Copy `.env.example` to `.env`
4. Test setup: `cd topic-1.1-text-preprocessing/exercises && python demo_solution.py`

**Week 1: Text Preprocessing**
- Read: [Topic 1.1 README](topic-1.1-text-preprocessing/README.md)
- Complete: Topic 1.1 exercises (demo → practice1 → practice2)

**Week 2: Similarity & Classification**
- Complete: [Topic 1.2](topic-1.2-semantic-similarity/) exercises
- Complete: [Topic 1.3](topic-1.3-ner-classification/) exercises

**Week 3: RAG & GenAI**
- Complete: [Topic 1.4](topic-1.4-rag/) exercises

### For Instructors

**Planning** (30 minutes)
1. Review [EXERCISE_CATALOG.md](EXERCISE_CATALOG.md) for all exercises
2. Read topic READMEs to understand learning objectives
3. Test run all solution files to verify they work

**Teaching Approach**
- Use topic READMEs as lecture content
- Demo solution files in class
- Assign exercise files as homework
- Use solution files for grading reference

---
   - Reference: Complete exercises in Topic 1.1
   - Follow: Same structure and documentation style

4. **Priority**
   - High: Topics 1.2 & 1.3 beginner levels
   - Medium: All intermediate levels
   - Lower: Advanced levels (for expert students)

---

## 📚 Complete File Structure

```
nlp-labs/
│
├── 📄 README.md                    ← Start here: Overview & setup
├── 📄 QUICK_START.md              ← Getting started guide
├── 📄 EXERCISE_CATALOG.md         ← All 28 exercises listed
├── 📄 IMPLEMENTATION_STATUS.md    ← What's done, what's next
├── 📄 INDEX.md                    ← This file
│
├── 🔧 requirements.txt             ← Python dependencies
├── 🔧 .env.example                 ← Azure OpenAI config template
├── 🔧 generate_exercises.py        ← Auto-generate skeletons
├── 🔧 generated_files.txt          ← List of generated files
│
├── 📁 topic-1.1-text-preprocessing/
│   ├── 📄 README.md               ← Topic concepts & objectives
│   ├── 📁 beginner/               ← 6 files (COMPLETE)
│   │   ├── demo_exercise.py
│   │   ├── demo_solution.py
│   │   ├── practice1_exercise.py
│   │   ├── practice1_solution.py
│   │   ├── practice2_exercise.py
│   │   └── practice2_solution.py
│   ├── 📁 intermediate/           ← 6 files (COMPLETE)
│   │   └── (same structure)
│   └── 📁 advanced/               ← 6 files (PARTIAL)
│       └── (same structure)
│
├── 📁 topic-1.2-semantic-similarity/
│   ├── 📄 README.md               ← Topic concepts
│   ├── 📁 beginner/               ← Skeleton + some complete
│   ├── 📁 intermediate/           ← Skeleton generated
│   └── 📁 advanced/               ← Skeleton generated
│
├── 📁 topic-1.3-ner-classification/
## 📁 Repository Structure

```
nlp-labs/
├── 📄 README.md                   ← Main documentation
├── 📄 QUICK_START.md              ← Getting started guide
├── 📄 EXERCISE_CATALOG.md         ← All exercises listed
├── 📄 INDEX.md                    ← This file
├── 📄 requirements.txt            ← Python dependencies
├── 📄 .env.example                ← Azure OpenAI config template
│
├── 📁 topic-1.1-text-preprocessing/
│   ├── README.md                  ← Concepts & objectives
│   └── exercises/
│       ├── demo_exercise.py
│       ├── demo_solution.py
│       ├── practice1_exercise.py
│       ├── practice1_solution.py
│       ├── practice2_exercise.py
│       └── practice2_solution.py
│
├── 📁 topic-1.2-semantic-similarity/
│   ├── README.md
│   └── exercises/ (6 files)
│
├── 📁 topic-1.3-ner-classification/
│   ├── README.md
│   └── exercises/ (6 files)
│
└── 📁 topic-1.4-rag/
    ├── README.md
    └── exercises/ (6 files)
```

**Total:** 4 topics × 6 exercise files = 24 exercise files + documentation

---

## 🗺️ Suggested Learning Path

### Week 1: Text Fundamentals
- **Topic 1.1**: Text Preprocessing
  - Demo: Basic preprocessing pipeline
  - Practice 1: Tokenization strategies
  - Practice 2: Bag of Words implementation

### Week 2: Similarity & Classification
- **Topic 1.2**: Semantic Similarity
  - Demo: Cosine similarity
  - Practice 1: Inverted index search
  - Practice 2: BM25 ranking

- **Topic 1.3**: NER & Classification
  - Demo: Rule-based NER
  - Practice 1: Sentiment analysis
  - Practice 2: Evaluation metrics

### Week 3: Advanced Integration
- **Topic 1.4**: RAG & GenAI
  - Demo: End-to-end NLP pipeline
  - Practice 1: BoW vs embeddings
  - Practice 2: RAG with Azure OpenAI

---

## 💻 Command Reference

### Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Configure Azure OpenAI (optional, for Topic 1.4)
copy .env.example .env
# Edit .env with your credentials
```

### Running Exercises
```bash
# Navigate to exercises folder
cd topic-1.1-text-preprocessing/exercises

# Try solving the exercise yourself
python demo_exercise.py

# Check the complete solution
python demo_solution.py
```

### Debugging in VS Code
1. Open an exercise file
2. Set breakpoints on TODO lines
3. Press F5 to start debugging
4. Step through code to understand flow

---

## 📚 Exercise Catalog Quick Links

### Topic 1.1: Text Preprocessing
- [Demo: Preprocessing Pipeline](topic-1.1-text-preprocessing/exercises/demo_exercise.py)
- [Practice 1: Tokenization](topic-1.1-text-preprocessing/exercises/practice1_exercise.py)
- [Practice 2: Bag of Words](topic-1.1-text-preprocessing/exercises/practice2_exercise.py)

### Topic 1.2: Semantic Similarity
- [Demo: Cosine Similarity](topic-1.2-semantic-similarity/exercises/demo_exercise.py)
- [Practice 1: Inverted Index](topic-1.2-semantic-similarity/exercises/practice1_exercise.py)
- [Practice 2: BM25 Ranking](topic-1.2-semantic-similarity/exercises/practice2_exercise.py)

### Topic 1.3: NER & Classification
- [Demo: Rule-Based NER](topic-1.3-ner-classification/exercises/demo_exercise.py)
- [Practice 1: Sentiment Analysis](topic-1.3-ner-classification/exercises/practice1_exercise.py)
- [Practice 2: Evaluation Metrics](topic-1.3-ner-classification/exercises/practice2_exercise.py)

### Topic 1.4: RAG & GenAI
- [Demo: End-to-End Pipeline](topic-1.4-rag/exercises/demo_exercise.py)
- [Practice 1: Embeddings Comparison](topic-1.4-rag/exercises/practice1_exercise.py)
- [Practice 2: Simple RAG](topic-1.4-rag/exercises/practice2_exercise.py)

---

## 🆘 Troubleshooting

**Installation Issues**
- Ensure Python 3.8+ is installed
- Use virtual environment: `python -m venv venv`
- Activate: `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Mac/Linux)

**Azure OpenAI Connection**
- Verify `.env` file has correct credentials
- Check endpoint URL format (should end with `.openai.azure.com/`)
- Ensure API key is valid
- Topics 1.1-1.3 work without Azure OpenAI

**Import Errors**
- Run `pip install -r requirements.txt` again
- Check for typos in package names
- Use `pip list` to verify installed packages

---

## 📖 Additional Resources

- [Python Official Docs](https://docs.python.org/3/)
- [NLTK Book](https://www.nltk.org/book/)
- [scikit-learn Tutorials](https://scikit-learn.org/stable/tutorial/index.html)
- [Azure OpenAI Documentation](https://learn.microsoft.com/en-us/azure/ai-services/openai/)

---

**Ready to start? Head to [QUICK_START.md](QUICK_START.md) for a 5-minute setup guide!**
```

---

## 📊 Exercise Difficulty Matrix

| Topic | Beginner | Intermediate | Advanced |
|-------|----------|--------------|----------|
| **1.1 Text Preprocessing** | ✅ Complete | ✅ Complete | ⚠️ Partial |
| **Concepts** | Basic cleaning | TF-IDF, Word2Vec | Subword, Production |
| **Time** | 2-3 hours | 3-4 hours | 4-5 hours |
|||
| **1.2 Semantic Similarity** | 📝 Skeleton | 📝 Skeleton | 📝 Skeleton |
| **Concepts** | Cosine, Index | Hybrid search | FAISS, Re-rank |
| **Time** | 2-3 hours | 3-4 hours | 4-5 hours |
|||
| **1.3 NER & Classification** | 📝 Skeleton | 📝 Skeleton | 📝 Skeleton |
| **Concepts** | Regex NER, Metrics | spaCy, ML models | LLM NER, BERT |
| **Time** | 2-3 hours | 3-4 hours | 5-6 hours |
|||
| **1.4 RAG & GenAI** | ✅ RAG Demo | 📝 Skeleton | 📝 Skeleton |
| **Concepts** | Simple RAG | Vector DB | Production |
| **Time** | 2-3 hours | 4-5 hours | 6-8 hours |

**Total Time Estimate**: 40-60 hours for complete curriculum

---

## 🎯 Learning Objectives by Topic

### Topic 1.1: Text Preprocessing and Representations
**You will learn to:**
- Clean and normalize text for NLP tasks
- Compare tokenization strategies (char, word, subword)
- Build Bag of Words and TF-IDF representations
- Train and use word embeddings (Word2Vec, GloVe)
- **Why it matters**: Foundation for all downstream NLP tasks

### Topic 1.2: Semantic Similarity and Information Retrieval
**You will learn to:**
- Calculate semantic similarity between texts
- Build inverted indexes for fast keyword search
- Implement BM25 ranking algorithm
- Combine keyword and vector search (hybrid)
- **Why it matters**: Core of RAG retrieval, search engines

### Topic 1.3: NER, Text Classification, and NLP Evaluation
**You will learn to:**
- Extract named entities from text
- Build text classification pipelines
- Calculate and interpret evaluation metrics
- Perform systematic error analysis
- **Why it matters**: Understanding what your model actually does

### Topic 1.4: Concept Consolidation and Bridge to GenAI
**You will learn to:**
- Build end-to-end NLP pipelines
- Implement RAG systems with vector databases
- Compare traditional NLP vs LLM approaches
- Evaluate GenAI systems properly
- **Why it matters**: Build production AI applications

---

## 🔗 Integration with Azure OpenAI

All exercises are designed to work with Azure OpenAI. You'll need:

1. **Azure OpenAI Resource**: Create at portal.azure.com
2. **Deployments**:
   - GPT-4 or GPT-3.5-turbo (for generation)
   - text-embedding-ada-002 (for embeddings)
3. **API Key & Endpoint**: From Azure portal
4. **Configuration**: Set in `.env` file

Used in:
- Topic 1.1 Advanced: Compare embeddings
- Topic 1.2 Intermediate+: Semantic search
- Topic 1.3 Advanced: LLM-based NER
- Topic 1.4 All levels: RAG pipelines

---

## 📞 Getting Help

### Setup Issues
1. Check [QUICK_START.md](QUICK_START.md) troubleshooting section
2. Verify Python version (3.8+)
3. Ensure all packages installed: `pip list`
4. Test Azure OpenAI connection separately

### Concept Questions
1. Read topic README for concept explanations
2. Review related exercises in earlier topics
3. Check solution files for implementation patterns
4. Search official documentation (linked in READMEs)

### Exercise Implementation
1. Read learning goals in exercise header
2. Check hints in TODO comments
3. Run code frequently to test progress
4. Compare with solution file structure
5. Don't hesitate to ask instructor!

---

## 🎉 What You Get

After completing these labs, you will:

✅ **Understand** core NLP concepts deeply
✅ **Implement** preprocessing pipelines from scratch
✅ **Build** text classification and NER systems
✅ **Create** RAG applications with vector search
✅ **Evaluate** both traditional and GenAI systems
✅ **Deploy** production-ready NLP solutions

**You'll be ready to**:
- Build production RAG systems
- Fine-tune LLMs for your domain
- Evaluate AI system quality
- Optimize NLP pipelines
- Interview for NLP/ML roles

---

## 📝 Feedback & Contributions

### Provide Feedback
- Report issues or bugs
- Suggest improvements
- Request additional exercises
- Share success stories

### Contribute
- Complete skeleton exercises
- Add new practice problems
- Improve documentation
- Create video tutorials
- Share on GitHub

---

## 🚀 Next Steps

### Right Now
1. Go to [QUICK_START.md](QUICK_START.md)
2. Set up your environment
3. Run your first exercise
4. Start learning!

### This Week
1. Complete Topic 1.1 beginner level
2. Try the RAG demo (Topic 1.4)
3. Experiment with your own data
4. Share progress with instructor

### This Month
1. Complete all beginner exercises
2. Progress to intermediate level
3. Build a small NLP project
4. Present your work

---

**Last Updated**: 2026-07-05
**Version**: 1.0
**Total Exercises**: 28 (21 files each)
**Total Code**: 8,000+ lines
**Status**: 81% Complete, Ready for Students!

**Happy Learning! 🎓📚🚀**
