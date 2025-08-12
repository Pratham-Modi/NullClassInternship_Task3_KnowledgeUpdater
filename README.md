# 🧠 Task 3: AI-Powered Knowledge Updater

This project empowers users to interact with a continuously evolving AI knowledge base combining local data storage with powerful language models.

This project is a smart and efficient **Knowledge Updater chatbot** that allows users to:

- 🔍 Ask questions on general topics  
- 🧠 Get answers from a **locally stored knowledge base (ChromaDB)**  
- 💬 Automatically fallback to **Google Gemini API** if no match is found  
- 📚 Easily **add new knowledge** by topic (from Wikipedia)

The entire system is built with an interactive **Streamlit** UI, and it continuously enhances its ability to answer questions over time.

---

## 🚀 Built With

- 🖥️ `Streamlit` – UI for chatbot interaction  
- 📚 `Wikipedia` + `sentence-transformers` – For topic data fetching and embedding  
- 🧠 `ChromaDB` – Vector store to hold embeddings  
- 🤖 `google-generativeai` – Gemini API fallback  
- 🔐 `python-dotenv` – For managing API keys securely

---

## ✨ Features

✅ Ask factual/general questions (e.g., "Who built the Taj Mahal?")  
✅ Embed and store new topics locally  
✅ Vector search for quick answer matching  
✅ Fallback to Gemini API if no match is found  
✅ Chat history is maintained in-app  
✅ Clean, user-friendly interface via Streamlit

---

## 🧱 Folder Structure

```
Task3_KnowledgeUpdater/
│
├── src/
│   ├── embedder.py        # Wikipedia data fetch + embedding
│   ├── vector_store.py    # ChromaDB operations
│   └── gemini_bot.py      # Gemini fallback handling
│
├── app.py                 # Streamlit UI and main logic
├── requirements.txt       # Required packages
├── .env                   # API key (Git-ignored)
└── README.md              # Project overview
```

---

## 🔧 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Pratham-Modi/NullClassInternship_Task3_KnowledgeUpdater
cd NullClassInternship_Task3_KnowledgeUpdater
```

### 2. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
venv\Scripts\activate  # For Windows
# OR
source venv/bin/activate  # For Mac/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your API Key in `.env`

Create a `.env` file and paste:

```env
GOOGLE_API_KEY=your_gemini_key_here
```

### 5. Run the Streamlit app

```bash
streamlit run app.py
```

---

## 💡 Example Usage

💬 **Q: Where is the Taj Mahal located and what is it made of and who built it?**  
📖 A: The Taj Mahal is located in Agra, India. It is made of white marble and was commissioned by Shah Jahan.

💬 **Q: Which is the sixth planet?**  
📖 A: Saturn is the sixth planet from the Sun.

💬 **Q: Who won the first FIFA World Cup?**  
📖 A: Uruguay won the first FIFA World Cup in 1930.

---

## 📌 Notes

⚙️ Stores and reuses knowledge intelligently  
📡 Automatically reaches out to Gemini when local info is missing  
🔒 `.env` is excluded via `.gitignore` to protect API keys  
📂 Runs locally with no external database setup required
📁 The `data/` folder is initially empty and gets populated automatically with fetched and processed topic data during app usage.

---

## 📦 requirements.txt

```
streamlit
wikipedia
sentence-transformers
chromadb
google-generativeai
python-dotenv
```

---

**Pratham Modi**  
📅 July 2025
