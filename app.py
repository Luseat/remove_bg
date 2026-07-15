import streamlit as st
from rembg import remove, new_session
from PIL import Image
import io
import os


# BAGIAN 1: KONFIGURASI HALAMAN (Tampilan Web)


if os.path.exists("icon.png"):
    ikon = Image.open("icon.png")
else:
    ikon = "✂️"

st.set_page_config(layout="wide", page_title="Penghapus Background (Tanpa API)", page_icon=ikon)

# Menampilkan logo di tengah (menggunakan kolom agar ukurannya kecil dan posisinya di tengah)
if os.path.exists("icon.png"):
    col_logo_kiri, col_logo_tengah, col_logo_kanan = st.columns([4, 1.5, 4])
    with col_logo_tengah:
        st.image("icon.png", use_container_width=True)


st.markdown("<h2 style='text-align: center;'>Aplikasi Penghapus Background Foto (Tanpa API & Gratis)</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Upload gambar kamu, dan biarkan AI menghapus background-nya secara otomatis dan aman (privasi terjaga).</p>", unsafe_allow_html=True)
st.write("") # Memberi sedikit jarak/spasi


# BAGIAN 2: PENGATURAN MODEL, BACKGROUND & UPLOAD

st.markdown("### ⚙️ Pengaturan")
model_choice = st.selectbox(
    "Pilih Model AI (Ganti jika hasil potongan berantakan/kurang rapi):",
    [
        "u2net (Default - Bagus untuk foto umum/benda)", 
        "isnet-anime (SUPER - Khusus Gambar Anime/Ilustrasi)", 
        "u2net_human_seg (Khusus Foto Manusia/Orang Asli)", 
        "silueta (Ringan & Cepat)"
    ]
)

# Pilihan warna background tambahan
bg_color_choice = st.selectbox(
    "Pilih Warna Latar Belakang (Cocok untuk Pas Foto/Formal):", 
    ["Transparan", "Merah (Formal)", "Biru (Formal)", "Putih"]
)

# Pilihan dropdown menjadi nama model asli yang dikenali oleh rembg
model_dict = {
    "u2net (Default - Bagus untuk foto umum/benda)": "u2net",
    "isnet-anime (SUPER - Khusus Gambar Anime/Ilustrasi)": "isnet-anime",
    "u2net_human_seg (Khusus Foto Manusia/Orang Asli)": "u2net_human_seg",
    "silueta (Ringan & Cepat)": "silueta"
}
selected_model_name = model_dict[model_choice]

st.markdown("### 🖼️ Upload Foto")
# st.file_uploader adalah widget untuk mengunggah file. 
my_upload = st.file_uploader("Pilih gambar (PNG, JPG, JPEG)", type=["png", "jpg", "jpeg"])

# Logika program: Jika pengguna sudah memilih dan mengunggah gambar...
if my_upload is not None:
    
    # Membuka gambar yang diunggah menggunakan library PIL (Pillow)
    original_image = Image.open(my_upload)
    
    # st.columns(2) digunakan untuk membagi layar menjadi 2 kolom utama (Kiri dan Kanan)
    col_kiri, col_kanan = st.columns(2)
    
    with col_kiri:
        # Menampilkan teks rata tengah dan gambar asli
        st.markdown("<h3 style='text-align: center;'>Gambar Asli</h3>", unsafe_allow_html=True)
        
        # Gambar tidak terlalu besar: Bungkus dalam sub-kolom
        _, sub_img_kiri, _ = st.columns([1, 3, 1])
        with sub_img_kiri:
            st.image(original_image, use_container_width=True)
        
        # Trik membuat tombol ke tengah: Membuat 3 sub-kolom (kosong, tombol, kosong)
        _, sub_tengah_kiri, _ = st.columns([1, 2, 1])
        with sub_tengah_kiri:
            # Tombol ditaruh di sub-kolom tengah biar rata tengah
            tombol_hapus = st.button("Hapus Background", use_container_width=True)
            
    # Jika tombol hapus diklik...
    if tombol_hapus:
        
        
        # BAGIAN 3: PROSES PENGHAPUSAN BACKGROUND
        
        with st.spinner(f"AI ({selected_model_name}) sedang memproses gambar... Mohon tunggu!"):
            # Membuat session baru berdasarkan model yang dipilih user
            ai_session = new_session(selected_model_name)
            
            # Menghapus background menggunakan model spesifik (Hasilnya masih Transparan/RGBA)
            result_image = remove(original_image, session=ai_session)
            
            # pewarnaan background jika user memilih selain "Transparan"
            if bg_color_choice != "Transparan":
                color_map = {
                    "Merah (Formal)": (255, 0, 0),    #  RGB Merah
                    "Biru (Formal)": (0, 0, 255),     #  RGB Biru
                    "Putih": (255, 255, 255)          #  RGB Putih
                }
                bg_color = color_map[bg_color_choice]
                
                # Bikin kanvas baru (layar kosong) dengan warna solid yang dipilih
                final_image = Image.new("RGBA", result_image.size, bg_color)
                
                # Tempelkan foto orang yang udah tanpa background ke atas kanvas warna tersebut
                # result_image ditaruh 2 kali karena parameter ke-3 itu berfungsi sebagai 'mask' (pemotong)
                final_image.paste(result_image, (0, 0), result_image)
            else:
                # Jika milih transparan, pakai hasil asli langsung
                final_image = result_image
            
            with col_kanan:
                # Menampilkan teks rata tengah dan gambar hasil
                st.markdown("<h3 style='text-align: center;'>Hasil Akhir</h3>", unsafe_allow_html=True)
                
                # Trik agar gambar tidak terlalu besar: Bungkus dalam sub-kolom
                _, sub_img_kanan, _ = st.columns([1, 3, 1])
                with sub_img_kanan:
                    st.image(final_image, use_container_width=True)
                
                
                # BAGIAN 4: FITUR DOWNLOAD HASIL
                
                # Siapkan 'wadah' kosong di memori komputer
                img_bytes = io.BytesIO()
                
                # Simpan gambar hasil ke dalam wadah tersebut dengan format PNG 
                final_image.save(img_bytes, format="PNG")
                
                # Trik membuat tombol ke tengah untuk tombol download
                _, sub_tengah_kanan, _ = st.columns([1, 2, 1])
                with sub_tengah_kanan:
                    st.download_button(
                        label="Download Gambar Hasil",
                        data=img_bytes.getvalue(),
                        file_name="gambar_hasil.png",
                        mime="image/png",
                        use_container_width=True
                    )
else:
    # Ini akan ditampilkan jika pengguna belum mengunggah gambar apa pun
    st.info("Silakan upload gambar terlebih dahulu untuk memulai.")


# BAGIAN 5: FOOTER (Copyright)

# Menambahkan jarak (spasi kosong) agar footer turun ke bawah
st.markdown("<br><br><br><br>", unsafe_allow_html=True)

st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray; margin-bottom: 5px;'>"
    "Copyright &copy; 2026 Hanifudin Robbani | All Rights Reserved."
    "</p>", 
    unsafe_allow_html=True
)
