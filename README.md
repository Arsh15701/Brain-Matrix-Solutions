
# 📰 Fake News Detection using Machine Learning

This project uses Natural Language Processing and Machine Learning to detect whether a news article is **Real** or **Fake**.

---

## 💡 Features
- Real-time fake news classification
- TF-IDF based feature extraction
- Machine learning using Random Forest / Logistic Regression
- Deployed as a Streamlit web app

---

## 📁 Dataset
We used the publicly available **Fake and Real News Dataset** from Kaggle:
- **Fake.csv**: Fake news articles
- **True.csv**: Real news articles

🔗 [Dataset on Kaggle](https://www.kaggle.com/clmentbisaillon/fake-and-real-news-dataset)

---

## 🧪 Model
- **Preprocessing**: Cleaned text, removed punctuation, lowercase
- **Vectorization**: TF-IDF
- **Algorithms**: Random Forest (best), Logistic Regression, Naive Bayes
- **Accuracy**: ~93%

---

## 🚀 Run the Streamlit App
```bash
pip install -r requirements.txt
streamlit run app.py
