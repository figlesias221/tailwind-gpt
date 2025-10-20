# Tailwind GPT - RAG Expert for Tailwind CSS

> Conversational AI expert for Tailwind CSS powered by Retrieval-Augmented Generation (RAG)

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![OpenAI](https://img.shields.io/badge/OpenAI-412991?logo=openai&logoColor=white)](https://openai.com/)
[![LlamaIndex](https://img.shields.io/badge/LlamaIndex-1C1C1C)](https://www.llamaindex.ai/)
[![Pinecone](https://img.shields.io/badge/Pinecone-000000)](https://www.pinecone.io/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue)](https://www.python.org/)

## 🎯 Overview

Tailwind GPT is an intelligent chatbot specialized in answering technical questions about Tailwind CSS. It leverages **Retrieval-Augmented Generation (RAG)** to enhance Large Language Model (LLM) responses with up-to-date, accurate information sourced directly from Tailwind CSS documentation.

RAG (Retrieval-Augmented Generation) addresses two major challenges faced by LLMs:
1. **Lack of sources** when answering questions
2. **Outdated information** as models aren't continuously updated

This framework enables LLMs to access the latest information from indexed documentation and provide referenced responses, delivering significant added value for users. It excels particularly in knowledge-intensive tasks.

![Demo](demo.png)

## ✨ Features

- **RAG-Powered Responses**: Combines retrieval from indexed Tailwind documentation with GPT-3.5-turbo generation
- **Conversational Interface**: Interactive chat built with Streamlit
- **Accurate & Referenced**: Responses grounded in official Tailwind CSS documentation
- **Vector Search**: Fast semantic search using Pinecone vector database
- **Comprehensive Evaluations**: Multiple evaluation notebooks for quality assessment:
  - Correctness evaluation
  - Faithfulness evaluation
  - Relevancy evaluation
  - Similarity evaluation
- **Production-Ready**: Structured codebase with clear separation of concerns

## 🏗️ Architecture

The project implements a two-stage RAG architecture:

![Architecture Diagram](arch.png)
*Source: LangChain*

### 1. Indexation Module
- **Data Source**: Tailwind CSS documentation (180+ text files)
- **Embedding Model**: HuggingFace `sentence-transformers/all-mpnet-base-v2`
- **Vector Store**: Pinecone cloud-based vector database
- **Framework**: LlamaIndex for document processing and indexing

### 2. Retrieval + Generation Module
- **Query Processing**: User questions processed through LlamaIndex
- **Retrieval**: Semantic search across indexed documentation
- **Generation**: OpenAI GPT-3.5-turbo generates contextual responses
- **Chat Mode**: React-based conversational agent with memory

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| **LLM** | OpenAI GPT-3.5-turbo |
| **Orchestration** | LlamaIndex |
| **Vector Database** | Pinecone |
| **Embeddings** | HuggingFace Sentence Transformers |
| **Frontend** | Streamlit |
| **Language** | Python 3.8+ |
| **NLP** | NLTK |

## 📋 Prerequisites

- Python 3.8 or higher
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))
- Pinecone API key ([Sign up here](https://www.pinecone.io/))

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/figlesias221/tailwind-gpt.git
cd tailwind-gpt
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Dependencies include:
- `streamlit` - Web interface
- `openai` - OpenAI API client
- `llama-index` - RAG orchestration framework
- `nltk` - Natural language processing
- `pinecone-client` - Vector database client

### 3. Set Up Environment Variables

Create a `.env` file or configure Streamlit secrets:

```bash
# For local development
OPENAI_API_KEY=your_openai_api_key_here
PINECONE_API_KEY=your_pinecone_api_key_here
```

For Streamlit Cloud deployment, add to `.streamlit/secrets.toml`:
```toml
openai_key = "your_openai_api_key_here"
pinecone_key = "your_pinecone_api_key_here"
```

### 4. Index the Documentation (First Time Setup)

Run the ingestion script to index Tailwind CSS documentation into Pinecone:

```bash
python ingestion.py
```

This will:
- Read all documentation files from the `data/` directory
- Generate embeddings using HuggingFace model
- Store vectors in Pinecone index named "tailwind-hugging"

### 5. Launch the Application

```bash
streamlit run streamlit_app.py
```

The app will be available at `http://localhost:8501`

## 📁 Project Structure

```
tailwind-gpt/
├── streamlit_app.py          # Main Streamlit application
├── ingestion.py              # Document indexing pipeline
├── requirements.txt          # Python dependencies
├── .env.example              # Environment variables template
├── data/                     # Tailwind CSS documentation (180+ files)
│   ├── accent-color.txt
│   ├── animation.txt
│   ├── aspect-ratio.txt
│   └── ...
├── evals/                    # Evaluation notebooks
│   ├── correctness_eval.ipynb
│   ├── faith_eval.ipynb
│   ├── relevancy_eval.ipynb
│   └── similarity_eval.ipynb
├── arch.png                  # Architecture diagram
└── demo.png                  # Demo screenshot
```

## 💬 Usage

1. **Start the app**: `streamlit run streamlit_app.py`
2. **Ask questions** about Tailwind CSS in the chat interface
3. **Get accurate answers** grounded in official documentation

**Example Questions:**
- "What is the border-radius utility in Tailwind?"
- "How do I create a responsive grid layout?"
- "Explain the difference between padding and margin utilities"
- "What are the available color classes for backgrounds?"

## 🧪 Evaluation

The project includes comprehensive evaluation notebooks in the `evals/` directory:

### Correctness Evaluation
Measures how accurately the model answers questions compared to ground truth.

### Faithfulness Evaluation
Assesses whether responses are grounded in the retrieved context without hallucination.

### Relevancy Evaluation
Evaluates if retrieved documents are relevant to the user's query.

### Similarity Evaluation
Compares semantic similarity between generated and expected responses.

Run evaluations:
```bash
jupyter notebook evals/correctness_eval.ipynb
```

## 🔧 Configuration

### Customize the LLM

Modify the `ServiceContext` in `streamlit_app.py`:

```python
service_context = ServiceContext.from_defaults(
    llm=OpenAI(
        model="gpt-4",  # Change model
        temperature=0.5,  # Adjust creativity
        system_prompt="Your custom system prompt"
    )
)
```

### Adjust Chat Behavior

Change the chat mode:
```python
chat_engine = index.as_chat_engine(
    chat_mode="react",  # Options: "simple", "react", "condense_question"
    verbose=True
)
```

### Update Vector Index

To re-index documentation after updates:
1. Add/modify files in `data/` directory
2. Run `python ingestion.py`
3. Restart the Streamlit app

## 📊 How RAG Works in This Project

1. **User Query**: User asks a question about Tailwind CSS
2. **Embedding**: Question is converted to a vector using the same embedding model
3. **Retrieval**: Pinecone searches for semantically similar documentation chunks
4. **Context Formation**: Retrieved chunks are formatted as context
5. **Generation**: GPT-3.5-turbo generates a response using the context
6. **Response**: User receives an accurate, referenced answer

## 🎓 Key Concepts

### Retrieval-Augmented Generation (RAG)
RAG combines the power of large language models with information retrieval. Instead of relying solely on the model's training data, RAG:
- Retrieves relevant information from a knowledge base
- Augments the prompt with retrieved context
- Generates more accurate, up-to-date responses

### Vector Databases
Pinecone stores document embeddings as high-dimensional vectors, enabling:
- Fast semantic search
- Scalable document retrieval
- Real-time updates

### LlamaIndex
LlamaIndex (formerly GPT Index) provides:
- Document loading and parsing
- Embedding generation
- Index management
- Query engines and chat interfaces

## 👥 Contributors

<table>
  <tr>
    <td align="center">
      <img src="https://avatars.githubusercontent.com/figlesias221?v=4?s=64" width="64px;" alt=""/>
      <br />
      <sub><b>Federico Iglesias</b></sub>
      <br />
      <a href="https://github.com/figlesias221/tailwind-gpt/commits?author=figlesias221" title="Code">💻</a>
    </td>
    <td align="center">
      <img src="https://avatars.githubusercontent.com/FranRossi?v=4?s=64" width="64px;" alt=""/>
      <br />
      <sub><b>Francisco Rossi</b></sub>
      <br />
      <a href="https://github.com/figlesias221/tailwind-gpt/commits?author=FranRossi" title="Code">💻</a>
    </td>
    <td align="center">
      <img src="https://avatars.githubusercontent.com/frandecu?v=4?s=64" width="64px;" alt=""/>
      <br />
      <sub><b>Francisco Decurnex</b></sub>
      <br />
      💻
    </td>
  </tr>
</table>

## 📚 Resources

- [LlamaIndex Documentation](https://docs.llamaindex.ai/)
- [Pinecone Documentation](https://docs.pinecone.io/)
- [OpenAI API Reference](https://platform.openai.com/docs)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Tailwind CSS Documentation](https://tailwindcss.com/docs)
- [RAG Paper (Lewis et al., 2020)](https://arxiv.org/abs/2005.11401)

## 📄 License

This project is available for educational and research purposes.

## 🙏 Acknowledgments

- **Tailwind CSS Team** for the excellent documentation
- **LlamaIndex** for the powerful RAG framework
- **OpenAI** for GPT-3.5-turbo
- **Pinecone** for vector database infrastructure
- **Streamlit** for the intuitive UI framework

---

**Built with modern AI technologies to make Tailwind CSS expertise accessible through conversation**
