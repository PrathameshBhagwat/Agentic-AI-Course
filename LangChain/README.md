# LangChain & Agentic AI Masterclass

A structured repository containing practical implementations, hands-on tasks, and documentation for **LangChain**, **LangChain Expression Language (LCEL)**, **Document Loaders**, **Text Splitters**, and **Agentic AI** workflows.

---

## 📁 Repository Structure

```
LangChain/
├── Documentation/
│   ├── Notes/                     # Lecture notes & study guides (PDFs)
│   │   ├── 1. LangChain.pdf
│   │   ├── 2. LangChain.pdf
│   │   ├── 3. Chain in LangChain.pdf
│   │   ├── 4. Runnable in LangChain.pdf
│   │   ├── 5. RAG in LangChain.pdf
│   │   └── LangChain - From LLMs to Agentic AI.pdf
│   └── Task/                      # Assignment briefs & requirements
│       ├── Chain ass.pdf
│       ├── Loader ass.pdf
│       ├── Runnable ass.pdf
│       └── structure_output_tasks.pdf
│
├── Task/                          # Hands-on exercises & assignments
│   ├── country.py                 # RunnableParallel demonstration
│   ├── foodInfo.py                # RunnableSequence demonstration
│   ├── greeting.py                # Sequential greeting workflow
│   ├── gtNumber.py                # RunnableBranch conditional logic
│   ├── productInfo.py             # RunnablePassthrough pipeline
│   ├── programmingLanguageInfo.py # Parallel info extraction
│   ├── studentIntro.py            # Passthrough & prompt chaining
│   ├── textLength.py              # Conditional branching on text
│   ├── loader1.py                 # TextLoader (college_rules.txt, students.txt)
│   ├── loader2.py                 # PyPDFLoader (1.LangChain.pdf)
│   ├── loader3.py                 # WebBaseLoader (web scraping)
│   ├── loader4.py                 # CSVLoader (products.csv, students.csv)
│   ├── splitter1.py               # RecursiveCharacterTextSplitter
│   ├── blogGeneration.py          # AI blog generator
│   ├── storyGeneration.py         # Creative story pipeline
│   ├── MovieInfo.py               # Movie analysis & info
│   ├── hospitalManage.py          # Hospital management workflow
│   ├── PatientInfo.py             # Patient intake & processing
│   ├── jobManagement.py           # Job management system
│   ├── jobCandidate.py            # Candidate resume evaluation
│   ├── libraryManage.py           # Library tracking workflow
│   ├── library.py                 # Library assistant
│   ├── studentManage.py           # Student management
│   ├── studentResult.py           # Result generation & grading
│   └── TopicInfo.py               # Topic analysis & keywords
│
├── chatbot.py                     # Interactive conversational assistant
├── context.py                     # Context injection & retrieval
├── dynamicprompt.py               # Dynamic prompt template usage
├── staticprompt.py                # Static prompt templates
├── promptTemplate.py              # ChatPromptTemplate configurations
├── gemini.py                      # Google Gemini chat model integration
├── geminillm.py                   # Google Gemini LLM wrapper
├── geminiStructureOutput.py       # Pydantic structured output with Gemini
├── huggingface.py                 # HuggingFace Hub / Endpoint integration
├── structureOutput.py             # Structured output parsing with Pydantic
├── .env.example                   # Environment variable template
├── .gitignore                     # Git ignore rules
└── requirements.txt               # Project dependencies
```

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/PrathameshBhagwat/Agentic-AI-Course-.git
cd Agentic-AI-Course-/LangChain
```

### 2. Create and Activate a Virtual Environment
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root of `LangChain/` (or copy from `.env.example`):
```bash
cp .env.example .env
```

Fill in your respective API keys:
```env
# Google Gemini API Key
GOOGLE_API_KEY=your_google_api_key_here

# Groq API Key
GROQ_API_KEY=your_groq_api_key_here

# Hugging Face API Token
HUGGINGFACEHUB_API_TOKEN=your_huggingfacehub_api_token_here
```

---

## 🛠️ Key Topics Covered

1. **Prompt Engineering & Templates**
   - `ChatPromptTemplate`, variable inputs, dynamic & static prompting.

2. **Multi-Model Support**
   - **Google Gemini** (`langchain-google-genai`)
   - **Groq** (`langchain-groq`)
   - **Hugging Face** (`langchain-huggingface`)

3. **LangChain Expression Language (LCEL)**
   - `RunnableSequence` (`|` operator): Sequential pipelines.
   - `RunnableParallel`: Concurrent execution of multiple prompts/chains.
   - `RunnablePassthrough`: Passing raw input down the chain.
   - `RunnableBranch`: Conditional routing and fallback decisions.

4. **Document Loaders & Text Splitting**
   - `TextLoader`, `PyPDFLoader`, `CSVLoader`, `WebBaseLoader`.
   - `RecursiveCharacterTextSplitter` with configurable chunk size and overlap.

5. **Structured Outputs**
   - Enforcing Pydantic schemas on LLM completions for deterministic JSON outputs.

---

## 🔒 Security Best Practices
- Keep `.env` out of version control (already configured in `.gitignore`).
- Never hardcode API keys or secrets in source files.
