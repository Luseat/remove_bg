import streamlit as st
from rembg import remove
from PIL import Image
import io

# ============================================
# BAGIAN 1: KONFIGURASI HALAMAN (Tampilan Web)
# ============================================
# st.set_page_config digunakan untuk mengatur judul tab di browser dan iconnya.
st.set_page_config(layout="wide", page_title="Penghapus Background (Tanpa API)")

# Menampilkan judul besar di web kita
st.write("## Aplikasi Penghapus Background Foto (Tanpa API & Gratis)")
st.write("Upload gambar kamu, dan biarkan AI menghapus background-nya secara otomatis dan aman (privasi terjaga).")

# ==========================================
# BAGIAN 2: FITUR UPLOAD GAMBAR
# ==========================================
# st.file_uploader adalah widget untuk mengunggah file. 
# type=["png", "jpg", "jpeg"] membatasi jenis file yang bisa dipilih.
my_upload = st.file_uploader("Pilih gambar (PNG, JPG, JPEG)", type=["png", "jpg", "jpeg"])

# Logika program: Jika pengguna sudah memilih dan mengunggah gambar...
if my_upload is not None:
    
    # Membuka gambar yang diunggah menggunakan library PIL (Pillow)
    # Ini seperti membuka foto di aplikasi galeri komputer sebelum diedit
    original_image = Image.open(my_upload)
    
    # st.columns(2) digunakan untuk membagi layar menjadi 2 kolom (Kiri dan Kanan)
    col1, col2 = st.columns(2)
    
    # Menampilkan teks dan gambar asli di Kolom 1 (Kiri)
    col1.write("### Gambar Asli")
    col1.image(original_image)
    
    # Membuat tombol proses. 
    # Logika: Jika tombol diklik, kode di dalam blok 'if' ini akan dijalankan.
    if col1.button("Hapus Background"):
        
        # ==========================================
        # BAGIAN 3: PROSES PENGHAPUSAN BACKGROUND
        # ==========================================
        
        # st.spinner memberi efek loading berputar (karena AI butuh waktu beberapa detik)
        with st.spinner("AI sedang memproses gambar... Mohon tunggu!"):
            # INI ADALAH INTI DARI APLIKASI:
            # Fungsi remove() dari library rembg akan secara ajaib memotong objek utama dan membuang background.
            result_image = remove(original_image)
            
            # Menampilkan teks dan gambar hasil di Kolom 2 (Kanan)
            col2.write("### Hasil Akhir")
            col2.image(result_image)
            
            # ==========================================
            # BAGIAN 4: FITUR DOWNLOAD HASIL
            # ==========================================
            # Gambar hasil (result_image) masih berupa objek PIL di dalam memori Python.
            # Agar bisa didownload oleh pengguna, kita harus mengubahnya menjadi format file gambar biasa (bytes).
            
            # Siapkan 'wadah' kosong di memori komputer
            img_bytes = io.BytesIO()
            
            # Simpan gambar hasil ke dalam wadah tersebut dengan format PNG 
            # (Format PNG wajib dipakai agar bagian background yang transparan tidak berubah jadi putih/hitam)
            result_image.save(img_bytes, format="PNG")
            
            # Menyiapkan tombol download yang mengambil data gambar dari wadah tadi
            col2.download_button(
                label="Download Gambar Transparan",
                data=img_bytes.getvalue(),
                file_name="hasil_remove_bg.png",
                mime="image/png"
            )
else:
    # Ini akan ditampilkan jika pengguna belum mengunggah gambar apa pun
    st.info("Silakan upload gambar terlebih dahulu untuk memulai.")
