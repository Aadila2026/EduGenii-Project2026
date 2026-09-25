# EduGenie: AI-Powered Learning Assistant 🧠✨

EduGenie is an interactive educational chatbot platform built to support school students with real-time academic tools. It uses a combination of localized machine learning and cloud-based AI to provide five specialized learning features.

## 🚀 Key Features
* **Q&A System:** Powered by Google Gemini to answer general academic queries instantly.
* **Smart Explanations:** Powered locally by `LaMini-Flan-T5` to break down complex topics into simple terms.
* **Text Summarization:** Compresses long study paragraphs into concise revision notes.
* **Quiz Generator:** Automatically constructs interactive multiple-choice tests from text inputs.
* **Adaptive Learning Paths:** Builds customized step-by-step study guides for any given topic.

## 🛠️ Project Structure
```text
EduGenie/
├── static/
│   └── style.css          # Frontend visual styling sheet
├── templates/
│   └── index.html         # Frontend user interface layouts
├── .env                   # Local secure API key storage file
├── explanation_module.py  # Local execution NLP script
├── learning_path.py       # Study roadmapping logic
├── main.py                # Centralized FastAPI backend hub
├── qna.py                 # Academic query answering engine
├── quiz_module.py         # JSON test generation component
├── README.md              # Project documentation file
├── requirements.txt       # Necessary library dependency manifest
└── summary_module.py      # Content compression controller
```

## ⚙️ Installation and Setup
1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Add Environment Credentials:**
   Create a `.env` file in the root directory and append your key:
   ```text
   GEMINI_API_KEY=your_actual_api_key_here
   ```
3. **Run the Server Application:**
   ```bash
   uvicorn main:app --reload
   ```
4. **Access the Web Interface:**
   Open your browser and navigate to `http://127.0.0.1:8000`