import streamlit as st
from login import login_dengan_username_password, login_dengan_wajah, login_dengan_suara

st.set_page_config(page_title="Login", layout="centered")
st.title("🔐 Login Prediksi Diabetes")

# Inisialisasi session
if "login_berhasil" not in st.session_state:
    st.session_state.login_berhasil = False

# Form login
if not st.session_state.login_berhasil:
    st.subheader("Silakan pilih metode login")
    opsi = st.radio("Metode Login", ["Username & Password", "Login dengan Wajah", "Login dengan Suara"])

    if opsi == "Username & Password":
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if login_dengan_username_password(username, password):
                st.success("✅ Login berhasil!")
                st.session_state.login_berhasil = True
                st.rerun()
            else:
                st.error("❌ Username atau password salah.")

    elif opsi == "Login dengan Wajah":
        if st.button("Login Wajah"):
            berhasil, pesan = login_dengan_wajah()
            if berhasil:
                st.success(pesan)
                st.session_state.login_berhasil = True
                st.rerun()
            else:
                st.error(pesan)

    elif opsi == "Login dengan Suara":
        if st.button("Login Suara"):
            berhasil, pesan = login_dengan_suara()
            if berhasil:
                st.success(pesan)
                st.session_state.login_berhasil = True
                st.rerun()
            else:
                st.error(pesan)

    st.stop()

# Jika login berhasil
st.success("✅ Anda sudah login! Silakan buka halaman **Prediksi Diabetes** dari sidebar.")
