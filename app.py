import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. SETTING TAMPILAN (SLATE NAVY & MODERN)
st.set_page_config(page_title="Lensa AI Pro v1.7", page_icon="🌙")

st.markdown("""
    <style>
    .stApp { background-color: #0f172a; color: white; }
    .stButton>button { background: linear-gradient(45deg, #0ea5e9, #22d3ee); color: white; border: none; width: 100%; border-radius: 10px; height: 50px; font-weight: bold; }
    input { background-color: #1e293b !important; color: white !important; }
    </style>
    """, unsafe_allow_html=True)

# 2. LOGIN SYSTEM
if 'login' not in st.session_state:
    st.session_state.login = False

if not st.session_state.login:
    st.title("🌙 Lensa AI Pro v1.7")
    st.write("Premium Sharia-Compliant Product Photography")
    pw = st.text_input("Masukkan Master Password", type="password")
    if st.button("Masuk Aplikasi"):
        if pw == "LensaAIPRO_faal125":
            st.session_state.login = True
            st.rerun()
        else:
            st.error("Password Salah!")
    st.stop()

# 3. KONFIGURASI AI (Ganti 'ISI_API_KEY_KAMU' dengan API Key dari AI Studio)
genai.configure(api_key="ISI_API_KEY_KAMU")

st.title("📸 Lensa AI Pro Dashboard")
st.write("---")

# 4. INPUT USER
uploaded_file = st.file_uploader("Unggah Foto Produk", type=["jpg", "jpeg", "png"])
style = st.selectbox("Pilih Style Fotografi", ["Clean Minimalist", "Flat Lay", "Dark Moody", "Soft Aesthetic", "Cyberpunk Neon"])

# 5. EKSEKUSI MAGIC
if st.button("Generate Foto ✨"):
    if uploaded_file is not None:
        with st.spinner('Lensa AI sedang bekerja...'):
            img = Image.open(uploaded_file)
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            # Master Prompt v1.6 kamu
            prompt = f"Ubah foto produk ini menjadi gaya {style}. Aturan: Sharia-compliant, tidak ada aurat/manusia, pencahayaan studio premium, 8k resolution."
            
            response = model.generate_content([prompt, img])
            st.image(img, caption="Foto Asli", width=300)
            st.subheader("Hasil Lensa AI Pro:")
            st.write(response.text) # Nanti bisa diatur untuk menampilkan gambar hasil
    else:
        st.warning("Upload foto dulu bos!")
