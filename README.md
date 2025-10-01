# LangGraph Chatbot

A fully featured chatbot built using **LangGraph** with support for **threaded conversations, real-time streaming responses, vector database integration, and custom tools**. The project also includes a **Streamlit frontend** for an interactive user experience and **LangSmith integration** for tracing, monitoring, and cost analysis.  

---

## Features  

### Threading  
- Each conversation is stored with context, enabling **multi-turn threaded discussions**.  
- Users can revisit previous threads and continue conversations seamlessly.  

### Streaming  
- The chatbot streams tokens in **real-time**, allowing responses to appear progressively instead of waiting for the entire answer to be generated.  
- Improves user engagement and mimics natural chat flow.  

### Vector Database (SQLite + Embeddings)  
- **SQLite** is used as a lightweight vector store for embeddings.  
- Enables **semantic search and retrieval-augmented generation (RAG)** to improve chatbot accuracy with contextual knowledge.  
- Ideal for local development without external dependencies.  

### Tools Integrated  
1. **Web Search Tool** → Fetch up-to-date information from the internet with **DuckDuckGo**.  
2. **Calculator Tool** → Perform mathematical computations on-the-fly with **Custom Tool**.  
3. **Stock Price Tool** → Fetch real-time stock/share prices for financial queries with **Alpha Vantage API**.

### Frontend (Streamlit)  
- Clean and simple **Streamlit-based UI** for better user interaction.  
- Allows chatting with the bot in a conversational interface with history tracking.  

### LangSmith Integration  
- Complete workflow tracing with **LangSmith**.  
- Monitor:  
  - Latency per step  
  - Token usage (input & output)  
  - Cost tracking  
  - Workflow visualization  
- Provides deep observability into the chatbot’s performance.  

---

## Tech Stack  

- **LangGraph** → Workflow orchestration for LLMs  
- **LangChain** → LLM tooling & integrations  
- **SQLite** → Local database & vector store  
- **Streamlit** → Frontend UI  
- **LangSmith** → Tracing & monitoring  
- **Google Gemini API** → LLM backbone  

---

## Getting Started  

### 1️⃣ Clone the repository  
```bash
git clone https://github.com/tahirkorma/langgraph-chatbot.git
cd langgraph-chatbot
```

### 2️⃣ Create and activate a virtual environment  
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set up environment variables
```bash
Create a .env file in the root directory and configure the following:
GOOGLE_API_KEY=your_google_api_key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT='https://api.smith.langchain.com'
LANGCHAIN_API_KEY=your_langsmith_api_key
```

### 5️⃣ Run the Streamlit app
```bash
streamlit run app.py
```

### Future Improvements
+ Add authentication and user sessions
+ Expand vector DB support (e.g., Pinecone, Weaviate, FAISS)
+ Multi-agent workflows for complex queries
+ Dashboard for monitoring LangSmith traces
