# Aplikasi Penghapus Background Foto (Non-API & Gratis) ✂️🖼️

Aplikasi web canggih yang dibangun menggunakan **Python** dan **Streamlit** untuk menghapus latar belakang (background) gambar secara instan.

Berbeda dengan layanan berbayar, aplikasi ini **100% GRATIS dan TANPA LIMIT**. Proses penghapusan background dilakukan secara lokal di komputer Anda menggunakan *library* `rembg`, sehingga privasi gambar Anda terjamin aman.

## ✨ Fitur Utama
* **Gratis & Tanpa Batas:** Hapus background jutaan foto tanpa perlu berlangganan.
* **Privasi 100% Terjaga:** Pemrosesan gambar dilakukan secara offline di mesin Anda (lokal).
* **Banyak Pilihan Model AI:** 
  * `u2net` (Default): Sangat bagus untuk foto benda atau manusia secara umum.
  * `isnet-anime`: Spesialis memotong background dari gambar 2D, anime, kartun, atau ilustrasi.
  * `u2net_human_seg`: Fokus memotong foto orang/manusia.
  * `silueta`: Model yang ringan dan sangat cepat.
* **Warna Background Khusus (Pas Foto):** Selain hasil transparan (PNG), Anda juga bisa langsung menempelkan subjek pada latar belakang warna **Merah, Biru, atau Putih** (sangat cocok untuk keperluan pas foto formal/KTP/Ijazah).
* **Tampilan (UI) Rapi & Estetik:** Posisi gambar, tombol, dan teks sudah disesuaikan agar proporsional di layar, lengkap dengan logo custom dan footer hak cipta.

## ⚙️ Persyaratan Sistem
Pastikan Anda sudah menginstal:
* [Python](https://www.python.org/downloads/) (Disarankan versi 3.8 ke atas)

## 🚀 Cara Menjalankan Aplikasi (Lokal)

1. Buka Terminal atau Command Prompt (CMD).
2. Masuk ke direktori proyek seperti ini:
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
5. *Browser* Anda akan otomatis terbuka dan menampilkan aplikasi (biasanya di `http://localhost:8501`).

> **Catatan Penting:** Saat Anda menggunakan salah satu model AI untuk **pertama kalinya** (misalnya saat pertama kali memilih `isnet-anime`), prosesnya mungkin memakan waktu 1-2 menit karena sistem akan mengunduh file model AI (sekitar ~170MB) tersebut secara otomatis. Untuk gambar kedua dan seterusnya, prosesnya akan berjalan sangat cepat!

## 🖼️ Kustomisasi Ikon
Anda dapat mengganti logo/ikon aplikasi dengan gambar Anda sendiri. Cukup simpan file gambar Anda ke dalam folder proyek ini dan beri nama **`icon.png`**. Aplikasi akan secara otomatis mendeteksinya dan menjadikannya sebagai logo aplikasi (di bagian atas halaman dan di icon tab browser).

## 🌐 Cara Deploy (Hosting) ke Streamlit Community Cloud
Jika Anda ingin menghosting aplikasi ini secara gratis agar bisa diakses semua orang dari HP atau komputer lain:
1. *Upload* seluruh file di direktori ini ke *repository* GitHub Anda (Pastikan `requirements.txt`, `app.py`, dan `icon.png` ter-upload).
2. Kunjungi [Streamlit Community Cloud](https://share.streamlit.io/).
3. Login menggunakan akun GitHub Anda.
4. Klik **New App**, pilih *repository* tempat Anda menyimpan *file* tadi.
5. Pastikan *Main file path* terisi dengan `app.py`.
6. Klik **Deploy** dan aplikasi Anda akan langsung *online*!

---
<p align="center">Copyright &copy; 2026 Hanifudin Robbani | All Rights Reserved.</p>
