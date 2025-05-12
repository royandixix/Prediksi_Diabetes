import streamlit as st
import numpy as np
import joblib

st.set_page_config(page_title="Prediksi Diabetes", layout="centered")

if "login_berhasil" not in st.session_state or not st.session_state.login_berhasil:
    st.warning("⚠️ Silakan login terlebih dahulu melalui halaman utama.")
    st.stop()

# Load model
try:
    model = joblib.load("model.pkl")
except FileNotFoundError:
    st.error("❌ File model tidak ditemukan (model.pkl).")
    st.stop()

st.markdown("<h1 style='text-align: center;'>📊 Prediksi Diabetes</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Masukkan data kesehatan Anda untuk memeriksa kemungkinan diabetes.</p>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

with st.form("form_prediksi"):
    col1, col2 = st.columns(2)
    with col1:
        Pregnancies = st.number_input("🤰 Jumlah Kehamilan", 0, 15, 1)
        Glucose = st.number_input("🍬 Kadar Glukosa", 50, 200, 100)
        BloodPressure = st.number_input("🩺 Tekanan Darah", 30, 130, 70)
        SkinThickness = st.number_input("📏 Ketebalan Kulit", 0, 100, 20)
    with col2:
        Insulin = st.number_input("💉 Kadar Insulin", 0, 900, 79)
        BMI = st.number_input("⚖️ BMI", 10.0, 70.0, 32.0)
        DPF = st.number_input("🧬 Riwayat Diabetes Keluarga (DPF)", 0.0, 2.5, 0.47)
        Age = st.number_input("🎂 Usia", 10, 100, 33)
    submitted = st.form_submit_button("🔍 Prediksi Sekarang")

if submitted:
    data = np.array([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DPF, Age]])
    prediction = model.predict(data)

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("### 🧾 Hasil Prediksi")
    if prediction[0] == 1:
        st.error("🔴 Anda kemungkinan menderita diabetes. Konsultasikan dengan dokter.")
    else:
        st.success("🟢 Anda kemungkinan tidak menderita diabetes. Jaga pola hidup sehat!")
