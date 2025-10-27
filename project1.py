import os
import tensorflow as tf
import numpy as np
from flask import Flask, request, jsonify
from PIL import Image
import io
from flask_cors import CORS
# Inisialisasi Aplikasi Flask
app = Flask(__name__)
# Tambahkan ini: Mengaktifkan CORS untuk semua domain dan semua endpoint
CORS(app)

# --- Konfigurasi dan Pemuatan Model ---

# Definisikan nama kelas (sesuai urutan di CIFAR-10)
CLASS_NAMES = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

# Path ke model
MODEL_PATH = 'cifar10_cnn_model.keras'

# Muat model Keras yang telah dilatih
try:
    model = tf.keras.models.load_model(MODEL_PATH)
    print("Model berhasil dimuat.")
except Exception as e:
    print(f"Gagal memuat model: {e}")
    model = None # Set None jika gagal

# Ukuran input yang diharapkan model (CIFAR-10)
IMG_HEIGHT = 32
IMG_WIDTH = 32

# Fungsi pra-pemrosesan gambar
def preprocess_image(image_bytes):
    # Buka gambar dari byte
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    # Ubah ukuran gambar
    image = image.resize((IMG_WIDTH, IMG_HEIGHT))
    # Konversi ke array numpy
    image_array = np.array(image)
    # Normalisasi (sesuai dengan preprocessing saat pelatihan)
    image_array = image_array / 255.0
    # Tambahkan dimensi batch (1, 32, 32, 3)
    image_array = np.expand_dims(image_array, axis=0)
    return image_array

# --- Endpoint API ---

@app.route('/predict', methods=['POST'])
def predict():
    # Cek ketersediaan model
    if model is None:
        return jsonify({'error': 'Model tidak ditemukan atau gagal dimuat'}), 500

    # Pastikan request memiliki file
    if 'file' not in request.files:
        return jsonify({'error': 'Tidak ada bagian file dalam request'}), 400

    file = request.files['file']
    
    # Pastikan nama file tidak kosong
    if file.filename == '':
        return jsonify({'error': 'Tidak ada file terpilih'}), 400

    if file:
        try:
            # Baca gambar sebagai byte
            img_bytes = file.read()
            
            # Pra-pemrosesan
            processed_image = preprocess_image(img_bytes)
            
            # Prediksi
            predictions = model.predict(processed_image)
            
            # Ambil indeks kelas dengan probabilitas tertinggi
            predicted_class_index = np.argmax(predictions[0])
            predicted_class_name = CLASS_NAMES[predicted_class_index]
            confidence = float(predictions[0][predicted_class_index])

            # Buat respons JSON
            response = {
                'prediction': predicted_class_name,
                'confidence': f"{confidence*100:.2f}%",
                'all_probabilities': {CLASS_NAMES[i]: float(predictions[0][i]) for i in range(len(CLASS_NAMES))}
            }
            return jsonify(response)

        except Exception as e:
            # Tangani error lain (misalnya format gambar yang salah)
            return jsonify({'error': f'Terjadi kesalahan saat memproses gambar: {str(e)}'}), 500

# Endpoint dasar untuk cek status
@app.route('/', methods=['GET'])
def home():
    return "API Klasifikasi Gambar CIFAR-10 Berjalan!"

# Jalankan aplikasi Flask
if __name__ == '__main__':
    # Jalankan pada port 5000 (default)
    app.run(host='0.0.0.0', port=5000)