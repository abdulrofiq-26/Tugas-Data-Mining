# 📊 Proyek Prediksi Churn Pelanggan Telco

## 📁 Struktur Repository
```
Tugas Data Maining/
├─ app.py                # Dashboard Streamlit
├─ tugas_datamining.py   # Skrip pembuatan data, pelatihan model, dan prediksi CLI
├─ churn_model.pkl       # Model Decision Tree yang sudah dilatih (dibuat setelah menjalankan script)
├─ scaler.pkl            # Scaler (StandardScaler) untuk fitur
├─ requirements.txt      # Daftar paket Python yang dibutuhkan
└─ README.md             # <‑‑ INI ADALAH README
```
## Dokumentasi

Berikut ini dokumentasi proyek mencakup:

- Latar belakang
- Tujuan pembuatan Data Mining
- Tahapan pembangunan Data Mining (Data Preparation, Modelling, Evaluation, Deployment)
- Screenshot hasil masing‑masing tahapan

## 🛠️ Prasyarat
- **Windows 10/11**
- **Python 3.13** (download dari https://www.python.org/downloads/windows/)
- **Git** (opsional, bila ingin meng‑clone repo)

## 🚀 Cara Memulai (Satu Baris Perintah)
```powershell
# 1️⃣ Buka PowerShell di folder proyek
cd "C:\Users\abdul\Downloads\Tugas Data Maining"

# 2️⃣ Buat virtual environment bersih (pakai interpreter Python 3.13 yang sudah terpasang) "sesuaikan dengan letak folder python di komputer anda"
C:\Users\abdul\AppData\Local\Programs\Python\Python313\python.exe -m venv .venv

# 3️⃣ Aktifkan environment
.\.venv\Scripts\Activate.ps1   # PowerShell
# (Jika pakai cmd, jalankan .\.venv\Scripts\activate.bat)

# 4️⃣ Install semua paket yang dibutuhkan
pip install -r requirements.txt

# 5️⃣ Latih model (akan menghasilkan churn_model.pkl & scaler.pkl)
python tugas_datamining.py

# 6️⃣ Jalankan dashboard Streamlit
streamlit run app.py
```

## 📋 Langkah‑langkah Detail
1. **Clone / Download Repository** – Jika Anda belum memiliki folder ini, jalankan:
```bash
git clone https://github.com/username/tugas-data-maining.git
cd tugas-data-maining
```
2. **Buat & Aktifkan Virtual Environment** (lihat perintah di atas).
3. **Pasang Dependensi** – File `requirements.txt` berisi:
```
numpy
pandas
scikit-learn
joblib
streamlit
```
   Jalankan `pip install -r requirements.txt`.
4. **Latih Model** – Skrip `tugas_datamining.py` akan:
   - Membuat data sintetis dengan pola churn logis (biaya tinggi + masa berlangganan pendek → risiko churn tinggi).
   - Membagi data menjadi training & test, men‑scale, melatih Decision Tree (max_depth=4).
   - Menyimpan model ke `churn_model.pkl` dan scaler ke `scaler.pkl`.
5. **Jalankan Dashboard** – Perintah `streamlit run app.py` akan membuka halaman web (biasanya di `http://localhost:8501`). Gunakan panel kiri untuk memasukkan data pelanggan, lalu klik **🔍 PREDIKSI SEKARANG**.

## 🧩 Cara Kerja Kode
- **`tugas_datamining.py`**: Membuat data, melatih model, dan menyimpan artefak.
- **`app.py`**: UI Streamlit yang memuat model & scaler, meng‑encode input (Gender: Male=1, Female=0; Internet: DSL=0, Fiber Optic=1, No=2), melakukan scaling, lalu menampilkan prediksi dengan tampilan berwarna (CHURN merah atau LOYAL hijau).

## 🔧 Masalah Umum & Solusi
| Gejala | Solusi |
|--------|-------|
| `ModuleNotFoundError: No module named 'numpy'` | Pastikan virtual environment sudah di‑activate (`.venv\Scripts\Activate.ps1`) sebelum instalasi atau menjalankan skrip. |
| `FileNotFoundError: churn_model.pkl` | Jalankan `python tugas_datamining.py` dulu untuk menghasilkan file model dan scaler. |
| `python: command not found` | Pakai interpreter di dalam venv: `.venv\Scripts\python.exe` atau gunakan path lengkap. |
| UI Streamlit kosong | Pastikan `churn_model.pkl` dan `scaler.pkl` berada di folder yang sama dengan `app.py`. |

## 📦 Ekspor `requirements.txt`
Jika ingin menyimpan versi paket yang tepat, jalankan setelah instalasi:
```powershell
pip freeze > requirements.txt
```
Kemudian dapat meng‑install kembali dengan `pip install -r requirements.txt`.

---
### 🎉 Selamat mencoba!
Eksplorasi nilai‑nilai berbeda, lihat bagaimana skor churn berubah, atau kembangkan proyek (misalnya coba classifier lain, tambahkan fitur, atau pakai data nyata).

*Selamat coding!*

## Latar Belakang

Data mining merupakan proses menemukan pola, anomali, dan informasi berguna dari kumpulan data yang besar. Pada proyek ini, kami menerapkan teknik data mining untuk memprediksi churn (perpindahan) pelanggan layanan telekomunikasi, sehingga perusahaan dapat mengambil langkah proaktif untuk mempertahankan pelanggan.

## Tujuan Pembuatan Data Mining

- Membangun model prediksi churn yang akurat menggunakan data sintetis.
- Menyediakan dashboard interaktif yang dapat digunakan oleh tim bisnis untuk menguji skenario pelanggan.
- Memperlihatkan alur lengkap dari persiapan data hingga deployment.

## Tahapan Pembangunan Data Mining

### 1. Data Preparation

Tahap pertama melibatkan pembuatan data sintetis, pembersihan, dan transformasi fitur. Data disimpan dalam format CSV dan ditampilkan pada tabel serta visualisasi distribusi churn.

![Data Preparation Screenshot](file:///c:/Users/abdul/.gemini/antigravity-ide/brain/fdc336e0-6bf6-491b-a346-2c18b2263712/data_preparation_screenshot_1781362746415.png)

### 2. Modelling

Model Decision Tree dilatih menggunakan Scikit‑Learn dengan parameter `max_depth=4`. Model dan scaler disimpan sebagai file `.pkl`.

![Model Training Screenshot](file:///c:/Users/abdul/.gemini/antigravity-ide/brain/fdc336e0-6bf6-491b-a346-2c18b2263712/model_training_screenshot_1781362765540.png)

### 3. Evaluation

Setelah pelatihan, model dievaluasi menggunakan metrik akurasi, precision, recall, dan confusion matrix pada data test. Hasil evaluasi ditampilkan pada console dan dapat dilihat pada dashboard.

### 4. Deployment

Dashboard dibangun dengan Streamlit. Pengguna dapat memasukkan atribut pelanggan dan memperoleh prediksi churn secara real‑time.

```powershell
streamlit run app.py
```

Setelah perintah dijalankan, buka browser pada `http://localhost:8501` untuk berinteraksi dengan aplikasi.

---
