# 🖼️ Klasifikasi Gambar Sederhana: CNN Deployment (TensorFlow & Flask)

Proyek ini mendemonstrasikan proses end-to-end Deep Learning: mulai dari pelatihan model Convolutional Neural Network (CNN) dasar menggunakan TensorFlow/Keras hingga deployment model sebagai RESTful API menggunakan Flask, dan antarmuka front-end sederhana berbasis HTML/JavaScript untuk pengujian langsung di browser.

Model ini dilatih pada dataset CIFAR-10, yang mengklasifikasikan 10 kategori objek (pesawat, mobil, burung, kucing, rusa, anjing, katak, kuda, kapal, truk).

---

## 🚀 Fitur Utama

- **Pelatihan Model CNN Dasar:** Model dibangun menggunakan lapisan `Conv2D` dan `MaxPooling` untuk klasifikasi 10 kelas.
- **Deployment API Cepat:** API Flask dengan endpoint `/predict` yang menerima gambar melalui POST request dan mengembalikan hasil klasifikasi dalam format JSON.
- **Antarmuka Web Interaktif:** Halaman `index.html` memungkinkan pengguna mengunggah gambar, melihat pratinjau, dan mendapatkan prediksi real-time dari API.
- **Data CIFAR-10:** Menggunakan dataset bawaan TensorFlow untuk kemudahan replikasi.

---

## 🛠️ Teknologi yang Digunakan

| Kategori | Pustaka/Framework | Tujuan |
|-----------|------------------|--------|
| Deep Learning | TensorFlow, Keras | Pelatihan dan loading model CNN. |
| Backend/API | Flask, Flask-CORS | Membuat endpoint API dan menangani permintaan lintas domain. |
| Pre-processing | Pillow (PIL), NumPy | Penanganan dan transformasi gambar. |
| Front-end | HTML, JavaScript | Antarmuka pengguna dan komunikasi ke API. |

---

## 📦 Struktur Proyek

```
klasifikasigambar/
├── app.py                      # Skrip utama API Flask (Backend)
├── cifar10_cnn_model.keras     # File model CNN yang sudah dilatih
├── index.html                  # Antarmuka web (Front-end)
├── training_cifar10.ipynb      # Jupyter Notebook untuk proses pelatihan
└── venv/                       # Lingkungan Virtual Python
```

---

## ⚙️ Persiapan dan Instalasi

### 1. Klon Repositori

```bash
git clone https://github.com/YourUsername/klasifikasigambar.git
cd klasifikasigambar
```

### 2. Buat dan Aktifkan Lingkungan Virtual (Venv)

Sangat disarankan menggunakan venv untuk mengisolasi dependensi.

```bash
# Buat venv
python -m venv venv

# Aktifkan venv (Windows PowerShell)
.env\Scriptsctivate

# Aktifkan venv (Linux/macOS)
# source venv/bin/activate
```

### 3. Instal Dependensi

Pastikan Anda berada di dalam `(venv)` saat menjalankan perintah instalasi ini:

```bash
(venv) pip install tensorflow keras numpy flask flask-cors pillow jupyter notebook
```

---

## 🚀 Langkah Menjalankan Proyek

### Langkah 1: Pelatihan Model

Jika file `cifar10_cnn_model.keras` belum ada, Anda harus melatih model:

Jalankan Jupyter Notebook:

```bash
(venv) jupyter notebook
```

Buka dan jalankan semua sel di `training_cifar10.ipynb`. Model akan diunduh, dilatih, dan disimpan di direktori utama.

### Langkah 2: Menjalankan API Flask

Buka terminal dan jalankan server API. Biarkan terminal ini tetap terbuka:

```bash
(venv) python app.py
```

Server akan mulai berjalan, biasanya di `http://127.0.0.1:5000`.

### Langkah 3: Pengujian di Browser

Buka antarmuka front-end di browser Anda:

- Buka file `index.html` di browser web Anda (misalnya, klik dua kali file tersebut).
- Unggah gambar uji.
- Klik **"Klasifikasikan Gambar"** untuk melihat hasil prediksi dari model.

---

## 📝 Dokumentasi API

Anda dapat mengirim permintaan **POST** langsung ke endpoint prediksi menggunakan alat seperti **curl** atau **Postman**.

| Metode | Endpoint | Deskripsi |
|---------|-----------|-----------|
| **POST** | `/predict` | Menerima gambar dan mengembalikan klasifikasi. |
| **GET** | `/` | Cek status dasar server. |

### Contoh Uji cURL

```bash
curl -X POST -F "file=@path/ke/gambar/test_image.jpg" http://127.0.0.1:5000/predict
```

### Contoh Respons JSON

```json
{
  "prediction": "airplane",
  "confidence": "92.15%",
  "all_probabilities": {
    "airplane": 0.9215,
    "automobile": 0.01
  }
}
```
---

## 🤝 Kontribusi

Proyek ini didesain sebagai implementasi dasar. Kontribusi untuk meningkatkan akurasi model, efisiensi deployment, atau penyempurnaan front-end sangat diterima.

---

## 

## 📄 Lisensi

Proyek ini dirilis di bawah **Lisensi MIT**.
