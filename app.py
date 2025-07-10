import streamlit as st
import pickle
import re

# Load trained model and vectorizer
model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

# Function to clean user input
def clean_text(text):
    text = text.lower()
    text = re.sub(r'https?://\\S+|www\\.\\S+', '', text)  # remove URLs
    text = re.sub(r'[^a-z\\s]', '', text)                 # remove punctuation/numbers
    return text

# Prediction function
def predict_news(news_text):
    clean = clean_text(news_text)
    vec = vectorizer.transform([clean])
    prediction = model.predict(vec)
    return "🟢 Real News" if prediction[0] == 1 else "🔴 Fake News"

# Streamlit App UI
st.set_page_config(page_title="Fake News Detector", page_icon="📰")
st.title("📰 Fake News Detection App")
st.markdown("Enter a news article or paragraph, and the model will predict whether it's **Real** or **Fake**.")

# Input field
news_input = st.text_area("📝 Paste News Article Here", height=200)

# Predict button
if st.button("🔍 Predict"):
    if news_input.strip() == "":
        st.warning("⚠️ Please enter some text.")
    else:
        result = predict_news(news_input)
        st.success(f"Prediction: {result}")


