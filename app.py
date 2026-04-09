import streamlit as st
from PIL import Image
import fitz
import docx
import pytesseract
import re
import random

st.set_page_config(page_title="AI Text Detector", layout="centered")

# ------------------------------
# HEADER
# ------------------------------
st.title("🧠 AI Text Detector")
st.caption("Upload a file or paste text to analyze AI likelihood")

# ------------------------------
# INPUT TYPE
# ------------------------------
option = st.radio(
    "Choose input type:",
    ["✍️ Manual Text", "📄 PDF", "📝 Word", "🖼️ Image"],
    horizontal=True
)

text = ""

# ------------------------------
# TEXT INPUT
# ------------------------------
if option == "✍️ Manual Text":
    text = st.text_area("Enter your text:", height=200)

# ------------------------------
# PDF INPUT
# ------------------------------
elif option == "📄 PDF":
    file = st.file_uploader("Upload PDF", type=["pdf"])
if file:
    with fitz.open(stream=file.read(), filetype="pdf") as doc:
        text = ""
        for page in doc:
            text += page.get_text()

    st.success("PDF loaded")

# ------------------------------
# WORD INPUT
# ------------------------------
elif option == "📝 Word":
    file = st.file_uploader("Upload Word file", type=["docx"])
    if file:
        doc = docx.Document(file)
        text = "\n".join([p.text for p in doc.paragraphs])
        st.success("Word file loaded")

# ------------------------------
# IMAGE INPUT (OCR)
# ------------------------------
elif option == "🖼️ Image":
    file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])
    if file:
        image = Image.open(file)
        st.image(image, caption="Uploaded Image", use_container_width=True)

        try:
            text = pytesseract.image_to_string(image)
            st.success("Text extracted from image")
        except:
            st.warning("OCR not supported in this environment")

# ------------------------------
# SHOW EXTRACTED TEXT
# ------------------------------
if text:
    with st.expander("📃 Extracted Text Preview"):
        st.write(text[:2000])

# ------------------------------
# FAKE MODEL (placeholder)
# Replace this later
# ------------------------------
def fake_predict(text):
    # simple heuristic simulation
    length = len(text.split())
    punctuation = len(re.findall(r"[.,;:!?]", text))
    variation = len(set(text.split()))

    score = min(1.0, (length/200 + punctuation/50 + variation/300))
    score = max(0.2, min(score, 0.9))

    # add slight randomness
    score = (score + random.uniform(-0.05, 0.05))

    return round(score, 3)

# ------------------------------
# EXPLANATION ENGINE
# ------------------------------
def explain(text, score):
    reasons = []

    if len(text.split()) > 150:
        reasons.append("Long, structured text")

    if len(set(text.split())) / (len(text.split()) + 1) < 0.4:
        reasons.append("Low vocabulary variation")

    if len(re.findall(r"\.", text)) > 10:
        reasons.append("Highly consistent sentence structure")

    if score > 0.7:
        reasons.append("Predictable phrasing patterns")

    if not reasons:
        reasons.append("Natural variation typical of human writing")

    return reasons

# ------------------------------
# DETECTION BUTTON
# ------------------------------
st.divider()

if st.button("🚀 Detect AI"):

    if not text:
        st.warning("Please provide input text")
    else:
        with st.spinner("Analyzing..."):
            score = fake_predict(text)

        # RESULT
        st.subheader(f"📊 AI Probability: {score*100:.2f}%")

        # PROGRESS BAR
        st.progress(score)

        # LABEL
        if score > 0.7:
            st.error("⚠️ Likely AI-generated")
        elif score > 0.5:
            st.warning("🤔 Possibly AI-generated")
        else:
            st.success("✅ Likely Human-written")

        # EXPLANATION
        st.subheader("🧠 Why this result?")
        reasons = explain(text, score)
        for r in reasons:
            st.write(f"- {r}")

        # NOTE
        st.caption("Note: Current model is a placeholder. Replace with trained model for real results.")