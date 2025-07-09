# 📰 Fake News Detection Pipeline

Proyek ini adalah end-to-end pipeline berbasis **Apache Airflow** yang digunakan untuk melakukan scraping berita dari berbagai sumber RSS, membersihkannya, menyimpannya di database, melatih model deteksi hoax, dan menyediakan antarmuka interaktif untuk prediksi menggunakan **Streamlit**.

---

## 🚀 Fitur

- Scraping otomatis berita harian dari Detik, Kompas, Antara
- Preprocessing teks (pembersihan dan filtering)
- Penyimpanan data di MongoDB (raw) dan PostgreSQL (cleaned)
- Training model **Logistic Regression** dengan TF-IDF
- API prediksi melalui script dan UI interaktif dengan Streamlit

---

## 🧱 Teknologi

- Python 3.10
- Apache Airflow
- MongoDB + PostgreSQL
- Pandas, Scikit-learn, Joblib
- Streamlit
- Docker + Docker Compose

---

## 🧪 Struktur Proyek

fake-news-detection-pipeline/
├── app/ # UI Streamlit
├── dags/ # Airflow DAG
├── notebooks/ # Notebook training model
├── scripts/ # Scraper, cleaner, prediction
├── models/ # Trained model (joblib)
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .gitignore
└── README.md


---

## ⚙️ Cara Menjalankan

###
```bash
1. Clone Repository
git clone https://github.com/USERNAME/fake-news-detection-pipeline.git
cd fake-news-detection-pipeline

2. Jalankan dengan Docker Compose
docker compose up --build

3. Akses UI Airflow
http://localhost:8080
Username: airflow, Password: airflow

4. Streamlit UI
pip install -r requirements.txt
streamlit run app/app.py

🔍 Contoh Prediksi
python scripts/predict.py "Pemerintah mengumumkan ada hari libur nasional baru."

👨‍💻 Author
Fakhri Azis Basiri
Data Engineer & Software Engineer