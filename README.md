# Aplikasi Penghapus Background (Non-API) ✂️🖼️

Aplikasi web sederhana yang dibuat menggunakan **Python** dan **Streamlit** untuk menghapus latar belakang (background) gambar secara instan.

Berbeda dengan layanan seperti remove.bg, aplikasi ini **100% GRATIS dan TANPA LIMIT**. Aplikasi ini menggunakan *library* `rembg` (berbasis model AI U^2-Net) yang memproses gambar secara lokal di perangkat Anda.

## ✨ Fitur Utama
* **Gratis Tanpa Batas:** Hapus background jutaan gambar tanpa perlu berlangganan.
* **Privasi 100% Terjaga:** Gambar diproses secara lokal di komputer Anda, tidak ada gambar yang diunggah ke *server* luar.
* **Offline Support:** Setelah model AI berhasil diunduh pada percobaan pertama, aplikasi bisa dijalankan tanpa koneksi internet.
* **Hasil Presisi:** Menggunakan model AI canggih untuk pemotongan objek yang rapi.
* **Transparansi Terjaga:** Gambar hasil akhir dapat diunduh dalam format PNG agar *background* tetap transparan.

## ⚙️ Persyaratan Sistem
Pastikan Anda sudah menginstal:
* [Python](https://www.python.org/downloads/) (Disarankan versi 3.8 ke atas)

## 🚀 Cara Menjalankan Aplikasi (Lokal)

1. Buka Terminal atau Command Prompt (CMD).
2. Masuk ke direktori proyek ini:
   ```bash
   cd path/ke/folder/remove-bg
   ```
3. Install semua *library* pendukung yang dibutuhkan:
   ```bash
   pip install -r requirements.txt
   ```
4. Jalankan aplikasi menggunakan Streamlit:
   ```bash
   streamlit run app.py
   ```
5. *Browser* Anda akan otomatis terbuka dan menampilkan aplikasi.

> **Catatan Penting:** Saat Anda menghapus *background* gambar untuk **pertama kalinya**, prosesnya mungkin memakan waktu agak lama karena aplikasi akan mengunduh model AI (U^2-Net) sebesar ~170MB secara otomatis. Untuk gambar kedua dan seterusnya, prosesnya akan sangat cepat!

## 🌐 Cara Deploy ke Streamlit Community Cloud
Jika Anda ingin menghosting aplikasi ini agar bisa diakses secara publik:
1. *Upload* seluruh *file* di direktori ini ke *repository* GitHub Anda (Pastikan `requirements.txt` ikut ter-*upload*).
2. Kunjungi [Streamlit Community Cloud](https://share.streamlit.io/).
3. Hubungkan akun GitHub Anda.
4. Klik **New App**, pilih *repository* Anda, dan arahkan *Main file path* ke `app.py`.
5. Klik **Deploy** dan aplikasi Anda akan segera *online* secara gratis!

---
*Dibuat oleh Hanifudin Robbani untuk keperluan edukasi dan produktivitas harian.*
