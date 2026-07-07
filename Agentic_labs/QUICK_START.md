# Quick Start Guide - NLP Labs

Get up and running with hands-on NLP exercises in 5 minutes.

---

## 🚀 Setup Steps

### Step 1: Install Dependencies

```bash
cd e:/ey-ai/nlp-labs
pip install -r requirements.txt
```

### Step 2: Download NLTK Data

```bash
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet')"
```

### Step 3: Configure Azure OpenAI (Optional)

**Note**: Only needed for Topic 1.4 exercises. Topics 1.1-1.3 work without Azure OpenAI.

```bash
copy .env.example .env
```

Edit `.env` with your credentials:
```env
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_API_KEY=your-key-here
AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4
AZURE_OPENAI_EMBEDDING_DEPLOYMENT=text-embedding-ada-002
```

### Step 4: Run Your First Exercise

```bash
cd topic-1.1-text-preprocessing/exercises
python demo_solution.py
```

You should see output showing text preprocessing results. Success! ✅

---

## 📚 What to Do Next

### Option 1: Follow the Structured Path (Recommended)

**Week 1**: Text Preprocessing
```bash
cd topic-1.1-text-preprocessing/exercises
python demo_exercise.py      # Try solving it yourself
python demo_solution.py      # Check the solution
python practice1_exercise.py # Practice tokenization
python practice2_exercise.py # Practice Bag of Words
```

**Week 2**: Similarity & Classification
```bash
cd ../topic-1.2-semantic-similarity/exercises
# Complete all 3 exercises

cd ../topic-1.3-ner-classification/exercises
# Complete all 3 exercises
```

**Week 3**: RAG & GenAI
```bash
cd ../topic-1.4-rag/exercises
# Complete all 3 exercises (requires Azure OpenAI)
```

### Option 2: Jump to Specific Topics

Pick topics based on your learning goals:
- **Need text preprocessing basics?** → Topic 1.1
- **Building search systems?** → Topic 1.2
- **Want to classify text?** → Topic 1.3
- **Interested in RAG/LLMs?** → Topic 1.4

---

## 💻 How to Work with Exercises
### Exercise Structure

Each exercise file includes:

**📝 Exercise File** (`*_exercise.py`)
- 🎯 **Learning Goals**: What you'll learn
- 📚 **Key Concepts**: Core topics covered
- ⏱️ **Time Estimate**: How long it takes
- 🔧 **VS Code Setup**: How to run and debug
- 📝 **TODO Instructions**: Step-by-step with hints
- 💡 **Expected Output**: What success looks like

**✅ Solution File** (`*_solution.py`)
- Complete working implementation
- Detailed comments explaining each step
- Example outputs and demonstrations
- Best practices and tips

### Workflow

1. **Read** the exercise file header to understand goals
2. **Implement** the TODO functions following hints
3. **Test** your code frequently with `python filename.py`
4. **Debug** using VS Code debugger (F5) if needed
5. **Compare** your solution with the provided solution file
6. **Experiment** with different inputs and parameters

---

## 🏗️ Repository Structure

```
nlp-labs/
├── README.md                         # Overview & documentation
├── QUICK_START.md                    # This file
├── EXERCISE_CATALOG.md               # All exercises listed
├── INDEX.md                          # Navigation guide
├── requirements.txt                  # Python dependencies
├── .env.example                      # Config template
│
├── topic-1.1-text-preprocessing/
│   ├── README.md
│   └── exercises/
│       ├── demo_exercise.py
│       ├── demo_solution.py
│       ├── practice1_exercise.py
│       ├── practice1_solution.py
│       ├── practice2_exercise.py
│       └── practice2_solution.py
│
├── topic-1.2-semantic-similarity/
│   ├── README.md
│   └── exercises/ (6 files)
│
├── topic-1.3-ner-classification/
│   ├── README.md
│   └── exercises/ (6 files)
│
└── topic-1.4-rag/
    ├── README.md
    └── exercises/ (6 files)
```

**Total:** 4 topics × 6 exercise files = **24 files**

---

## 🎯 Suggested Learning Schedule

### 📅 3-Week Plan (5-6 hours/week)

**Week 1: Text Fundamentals**
- Topic 1.1: Text Preprocessing (all 3 exercises)
- Practice time: 2-3 hours

**Week 2: Search & Classification**
- Topic 1.2: Semantic Similarity (all 3 exercises)
- Topic 1.3: NER & Classification (all 3 exercises)
- Practice time: 4-5 hours

**Week 3: Advanced Integration**
- Topic 1.4: RAG & GenAI (all 3 exercises)
- Practice time: 3-4 hours

### 📅 1-Week Intensive (15-18 hours)

**Days 1-2**: Topics 1.1 & 1.2  
**Days 3-4**: Topic 1.3  
**Days 5-7**: Topic 1.4 + review

---

## 🔧 Common Issues & Solutions

### `ImportError: No module named 'X'`
```bash
pip install -r requirements.txt
```

### `NLTK Data Not Found`
```bash
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet')"
```

### `Azure OpenAI Authentication Error`
- Verify `.env` file exists in the root directory
- Check endpoint URL format: `https://your-resource.openai.azure.com/`
- Ensure API key is active and has proper permissions
- **Note**: Only Topic 1.4 requires Azure OpenAI

### `Code Runs But Output Looks Wrong`
- Compare your implementation with the solution file
- Check for typos in variable names or function calls
- Use VS Code debugger (F5) to step through code
- Print intermediate results to verify logic

---

## 💡 Tips for Success

✅ **Do**:
- Read topic README before starting exercises
- Complete exercises in order (demo → practice1 → practice2)
- Run code frequently to catch errors early
- Use print statements to debug
- Compare with solutions after attempting yourself
- Experiment with different parameters

❌ **Don't**:
- Skip the demo exercises
- Copy solutions without understanding
- Move to next topic if current concepts are unclear
- Ignore error messages (they contain helpful info)

---

## 📖 Additional Resources

- [Main README](README.md) - Full repository overview
- [Exercise Catalog](EXERCISE_CATALOG.md) - All exercises with time estimates
- [Index](INDEX.md) - Detailed navigation guide
- Topic READMEs - Concept explanations for each topic

---

## 🆘 Need Help?

1. **Check solution files** for working implementations
2. **Read error messages** carefully (they often explain the issue)
3. **Review topic READMEs** for concept explanations
4. **Use VS Code debugger** to step through code
5. **Ask your instructor** if stuck

---

**Ready to start? Run your first exercise:**

```bash
cd topic-1.1-text-preprocessing/exercises
python demo_solution.py
```

Good luck with your NLP learning journey! 🚀
