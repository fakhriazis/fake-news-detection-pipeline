import pymongo
import psycopg2
import re
import nltk
from nltk.corpus import stopwords

# Download stopwords jika belum
nltk.download('stopwords')
stop_words = set(stopwords.words('indonesian'))

def clean_text(text):
    text = re.sub(r"<.*?>", "", text)  # hilangkan HTML
    text = re.sub(r"http\S+", "", text)  # hilangkan URL
    text = re.sub(r"[^a-zA-Z\s]", "", text)  # simbol
    tokens = text.lower().split()
    tokens = [word for word in tokens if word not in stop_words]
    return " ".join(tokens)

def process_data():
    # Koneksi MongoDB
    mongo = pymongo.MongoClient("mongodb://mongo:27017")  # untuk Docker
    news = mongo["fakenews"]["clean_news_raw"].find()

    # Koneksi PostgreSQL
    conn = psycopg2.connect(
        dbname="fakenews",
        user="postgres",
        password="123",
        host="postgres",  # untuk Docker
        port=5432
    )
    cur = conn.cursor()

    # Pastikan tabel tersedia
    cur.execute("""
        CREATE TABLE IF NOT EXISTS cleaned_news (
            id SERIAL PRIMARY KEY,
            title TEXT,
            content TEXT,
            published TEXT,
            source TEXT
        );
    """)
    conn.commit()

    for doc in news:
        cleaned = clean_text(doc.get("summary", ""))
        cur.execute("""
            INSERT INTO cleaned_news (title, content, published, source)
            VALUES (%s, %s, %s, %s)
        """, (
            doc.get("title", ""),
            cleaned,
            doc.get("published", ""),
            doc.get("source", "")
        ))

    conn.commit()
    cur.close()
    conn.close()
    print("News cleaned and saved to PostgreSQL.")

if __name__ == "__main__":
    process_data()
