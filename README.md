🤖 AI News Summarizer

An AI-powered application built with Python and Streamlit that transforms long-form articles into clear, concise summaries. It leverages Google Gemini API to extract key insights, generate structured summaries, and improve readability of dense text content.

🚀 Key Features
Paste article text and generate AI-based summaries
Extract important key points automatically
Estimate reading time for content
One-click copy functionality for generated output
Clean and responsive Streamlit interface
Dark mode support for better readability
Bonus utilities: quiz question generation and flashcard creation
🛠️ Tech Stack
Python
Streamlit
Google Gemini API
📂 Project Structure
News-Summarizer/
│── app.py
│── requirements.txt
│── .env
│── README.md
⚙️ Setup Instructions
1. Clone the repository
git clone <your-repo-link>
cd News-Summarizer
2. Install dependencies
pip install -r requirements.txt
3. Configure environment variables

Create a .env file and add your API key:

GEMINI_API_KEY=your_api_key_here
4. Run the application
streamlit run app.py
📌 Future Enhancements
Advanced summarization improvements using prompt tuning
Save and manage previous summaries
Export summaries in multiple formats (PDF/Docx)
User session memory and personalization
Scalable backend architecture integration
📄 License

This project is intended for learning and personal development purposes.
