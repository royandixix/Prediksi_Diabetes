# 🔐 Aplikasi Login Multi-Faktor Menggunakan Username, Deteksi Wajah, dan Suara

Aplikasi ini adalah sebuah sistem otentikasi (login) berbasis Python yang menggabungkan tiga metode login yang saling melengkapi yaitu: login menggunakan **username dan password**, **deteksi wajah secara real-time melalui kamera**, serta **verifikasi suara melalui pengenalan perintah suara**. Aplikasi ini sangat cocok digunakan sebagai proyek pembelajaran keamanan sistem informasi, dan dikembangkan menggunakan framework **Streamlit** agar dapat ditampilkan dalam bentuk antarmuka web yang sederhana dan mudah diakses.

---

## 🎯 Tujuan Aplikasi

Tujuan dari aplikasi ini adalah untuk memberikan pengalaman login yang lebih aman dan personal, dengan pendekatan berbasis **multi-faktor autentikasi (MFA)**. Dalam implementasinya, pengguna hanya akan bisa mengakses aplikasi jika berhasil melalui salah satu dari metode berikut:

1. **Login konvensional** menggunakan kombinasi _username dan password_.
2. **Login biometrik wajah** yang memanfaatkan kamera untuk mencocokkan wajah pengguna.
3. **Login berbasis suara**, dengan mengenali perintah suara spesifik yang sebelumnya telah direkam.

---

## 🏗️ Struktur Proyek


---

## ⚙️ Langkah Instalasi

Ikuti langkah-langkah berikut untuk menjalankan aplikasi di komputer Anda:

### 1. Clone Repositori GitHub
```bash
git clone https://github.com/username/nama-repo.git
cd nama-repo
📁 users/
├── wajah_user.jpg # File gambar wajah pengguna (harus terlihat jelas)
└── suara_login.wav # File rekaman suara untuk login (dengan kalimat tertentu)
📄 app.py # File utama aplikasi Streamlit
📄 requirements.txt # Daftar pustaka Python yang dibutuhkan
📄 README.md # Dokumentasi penggunaan aplikasi

python -m venv env
source env/bin/activate        # Linux/Mac
env\Scripts\activate           # Windows

pip install -r requirements.txt

🧪 Persiapan Data Pengguna

📷 Menyiapkan File Wajah
Ambil foto wajah pengguna secara jelas (tidak buram) dan simpan dengan nama wajah_user.jpg.
Pastikan file disimpan di folder users/.
Foto sebaiknya berisi satu wajah dengan pencahayaan yang cukup.
🎤 Menyiapkan File Suara
Rekam suara pengguna yang mengucapkan perintah login, misalnya:
"login royandi"
Simpan file rekaman tersebut dalam format .wav dengan nama suara_login.wav.
Tempatkan file tersebut di dalam folder users/.
Gunakan aplikasi seperti Audacity, perekam HP, atau tools online untuk membuat file .wav.


streamlit run app.py


http://localhost:8501


💡 Cara Menggunakan Aplikasi

Pilih metode login yang ingin digunakan:
Username dan password (default: royandi dan 123)
Deteksi wajah melalui kamera
Deteksi suara dengan perintah suara tertentu
Jika memilih deteksi wajah:
Pastikan kamera aktif
Sistem akan membandingkan wajah Anda dengan gambar di users/wajah_user.jpg
Jika memilih deteksi suara:
Sistem akan membaca file users/suara_login.wav
Hanya akan berhasil login jika ucapan cocok dengan kalimat seperti "login royandi"

📋 Contoh Isi requirements.txt

streamlit
numpy
opencv-python
speechrecognition
pydub


---

Kalau kamu sudah punya URL GitHub-nya, aku juga bisa bantu nulis versi pendek dan menarik untuk deskripsi halaman repo di bagian atas GitHub. Mau sekalian?
# Prediksi_Diabetes
