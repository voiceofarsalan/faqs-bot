# FAQs Bot using Google Palm and LangChain

This project is a question-answering chatbot built with [LangChain](https://www.langchain.com/) and [Google PaLM API](https://developers.generativeai.google/), designed to answer user queries based on a dataset of frequently asked questions (FAQs). It uses semantic search and retrieval-augmented generation (RAG) to fetch the most relevant responses.

---

## 🔧 Features

- Conversational interface powered by LangChain.
- Context-aware answers using Google's PaLM API.
- Fast semantic search using FAISS.
- Streamlit-powered UI for interactive experience.
- CSV-based knowledge ingestion (FAQs data).
- Modular and clean Python structure.

---

## 🧠 Technologies Used

- Python
- LangChain
- Google PaLM API
- Streamlit
- FAISS (Facebook AI Similarity Search)
- tiktoken
- dotenv

---

## 🗂 Dataset

The chatbot uses a structured FAQ dataset in CSV format (`codebasics_faqs.csv`), which contains questions and corresponding answers. This forms the base knowledge to be searched and retrieved for each user query.

---

## 🚀 Getting Started

### Prerequisites

Ensure you have Python 3.7+ and the following tools installed:
- pip
- Google PaLM API access and API key

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/your-username/faqs-bot.git
cd faqs-bot
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Set up environment variables**

Create a `.env` file with your Google API key:

```
GOOGLE_API_KEY=your-api-key-here
```

---

## 💻 Running the App

Use Streamlit to launch the chatbot interface:

```bash
streamlit run main.py
```

The app will open in your default browser at `http://localhost:8501`.

---

## 📂 File Structure

```
├── codebasics_faqs.csv         # FAQ dataset
├── main.py                     # Streamlit app
├── google_palm_codebasics_q_and_a.ipynb  # Model testing notebook
├── testfile.py                 # Sample/test utility
├── requirements.txt            # Required packages
├── .env                        # API keys (not tracked)
```

---

## ⚙️ Key Functionality

- **FAISS Embeddings:** For fast vector-based question matching.
- **LangChain + PaLM API:** Used to generate natural and accurate responses.
- **RAG (Retrieval-Augmented Generation):** Combines context search with LLM completion.

---

## 🧪 Example Use Cases

- Coding bootcamp or LMS chatbot for FAQs
- Customer service FAQ agents
- Support assistant for developer documentation

---

## 📜 License

This project is licensed under the MIT License. Feel free to use, modify, and share it for educational or commercial purposes.

---

## 🙌 Acknowledgements

Inspired by the [Codebasics YouTube Channel](https://www.youtube.com/c/codebasics), LangChain tutorials, and Google Generative AI tools.

---

## 📬 Contact

For any questions or collaboration:
**Arsalan Ahmed**  
Email: arsalanahmadofficial@gmail.com  
GitHub: [@voiceofarsalan](https://github.com/voiceofarsalan)
