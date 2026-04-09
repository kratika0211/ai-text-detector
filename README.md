🧠 AI Text Detector
A Streamlit-based web application that detects whether a piece of text is AI-generated or human-written.
Supports multiple input formats including manual text, PDF, Word documents, and images.

🚀 Features
✍️ Manual text input
📄 Upload PDF files
📝 Upload Word (.docx) documents
🖼️ Upload images (OCR supported locally)
📊 AI probability score (0–100%)
🧠 Explanation of why text is flagged
⚡ Fast and interactive UI

📂 Project Structure
ai-text-detector/
├──streamlit_app.py     # Main Streamlit UI
├──requirements.txt     # Dependencies
├──README.md            # Project documentation
└──ai_detector_model/   # (Optional) Trained model

⚙️ Installation (Local)
1. Clone the repository
git clone https://github.com/your-username/ai-text-detector.git
cd ai-text-detector
2. Install dependencies
pip install -r requirements.txt
3. (Optional) Enable OCR for images
Install Tesseract:
sudo apt install tesseract-ocr

For Windows:
Download from: https://github.com/tesseract-ocr/tesseract
4. Run the app
streamlit run streamlit_app.py

🌐 Deployment
This app can be deployed using:
Streamlit Cloud (recommended)
Hugging Face Spaces

🧠 How It Works
User uploads or inputs text
Text is extracted (PDF/Word/Image OCR)

Model analyzes patterns in:
Sentence Structure
Vocabulary Variation
Punctuation Patterns

Outputs:
AI probability score
Explanation of reasoning

🔮 Future Improvements
🔍 Highlight AI-generated sentences
📈 Confidence visualization
🤖 Integrate fine-tuned transformer model
🌐 Full deployment with backend API

🛠️ Tech Stack
Python
Streamlit
PyMuPDF (PDF processing)
python-docx
pytesseract (OCR)
Transformers (for future model integration)
🤝 Contributing

Pull requests are welcome!
For major changes, please open an issue first.

📄 License
This project is open-source and available under the MIT License.

👩‍💻 Author
Kratika Dariyani

⭐ If you like this project
Give it a ⭐ on GitHub!
