import streamlit as st
import joblib

# Load model & vectorizer
model = joblib.load("models/fake_news_model.pkl")
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")

# Judul Aplikasi
st.set_page_config(page_title="Deteksi Berita Hoax", layout="centered")
st.title("📰 Deteksi Berita Hoax")
st.markdown("Masukkan isi berita di bawah ini:")

# Input teks berita
text_input = st.text_area("Isi Berita", height=200)

if st.button("🔍 Prediksi"):
    if not text_input.strip():
        st.warning("Silakan masukkan isi berita terlebih dahulu.")
    else:
        text_vec = vectorizer.transform([text_input])
        prediction = model.predict(text_vec)[0]
        label = "🛑 HOAX" if prediction == 1 else "✅ ASLI"

        st.subheader("Hasil Prediksi:")
        st.success(label) if prediction == 0 else st.error(label)
