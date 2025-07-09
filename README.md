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

```
fake-news-detection-pipeline/
│
├── app/                  # UI Interaktif menggunakan Streamlit
│
├── dags/                 # DAG untuk Apache Airflow
│
├── notebooks/            # Notebook untuk training dan eksperimen model
│
├── scripts/              # Script untuk scraping, cleaning, dan prediction
│   ├── scrape_news.py
│   ├── clean_news.py
│   └── predict.py
│
├── models/               # Model hasil training (disimpan dalam format .joblib)
│
├── Dockerfile            # Dockerfile utama proyek
├── docker-compose.yml    # Docker Compose untuk orkestrasi layanan
├── requirements.txt      # Daftar dependency Python
├── .gitignore            # File untuk mengabaikan file/folder tertentu di Git
└── README.md             # Dokumentasi utama proyek
```


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