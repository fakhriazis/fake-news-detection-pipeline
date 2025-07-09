import joblib
import sys

# Load model dan vectorizer
model = joblib.load("models/fake_news_model.pkl")
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")

def predict(text):
    text_vec = vectorizer.transform([text])
    prediction = model.predict(text_vec)[0]
    label = "HOAX" if prediction == 1 else "ASLI"
    return label

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scripts/predict.py 'berita yang ingin diuji'")
        sys.exit(1)

    input_text = sys.argv[1]
    result = predict(input_text)
    print(f"\n📢 Prediksi: {result}\n")
