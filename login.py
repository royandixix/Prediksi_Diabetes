import streamlit as st
import numpy as np
import cv2
import speech_recognition as sr
import time
import os
from pydub import AudioSegment, silence

# ===== Login Username =====
def login_dengan_username_password(username, password):
    return username == "royandi" and password == "123"

# ===== Login Wajah =====
def login_dengan_wajah():
    path_wajah = "users/wajah_user.jpg"
    if not os.path.exists(path_wajah):
        return False, "❌ File wajah user tidak ditemukan"

    wajah_tersimpan = cv2.imread(path_wajah)
    wajah_tersimpan_resized = cv2.resize(wajah_tersimpan, (100, 100))

    st.info("📷 Mengaktifkan kamera untuk mendeteksi wajah secara real-time...")
    placeholder = st.empty()
    cam = cv2.VideoCapture(0)
    cocok = False
    selisih_final = 999.0

    if not cam.isOpened():
        return False, "❌ Kamera tidak bisa dibuka"

    start_time = time.time()
    while time.time() - start_time < 10:
        ret, frame = cam.read()
        if not ret:
            continue

        wajah_input_resized = cv2.resize(frame, (100, 100))
        selisih = np.mean(cv2.absdiff(wajah_input_resized, wajah_tersimpan_resized))
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        placeholder.image(frame_rgb, caption=f"Selisih wajah: {selisih:.2f}", use_container_width=True)

        if selisih < 30:
            cocok = True
            selisih_final = selisih
            break

    cam.release()
    placeholder.empty()

    if cocok:
        return True, f"✅ Wajah cocok (selisih {selisih_final:.2f})"
    else:
        return False, f"❌ Wajah tidak cocok (terakhir selisih {selisih:.2f})"

# ===== Potong suara login =====
def potong_sunyi(path_input, path_output):
    sound = AudioSegment.from_wav(path_input)
    nonsilent = silence.detect_nonsilent(sound, min_silence_len=300, silence_thresh=sound.dBFS-16)

    if nonsilent:
        start_trim = nonsilent[0][0]
        end_trim = nonsilent[-1][1]
        trimmed_sound = sound[start_trim:end_trim]
        trimmed_sound.export(path_output, format="wav")
    else:
        trimmed_sound = sound
        trimmed_sound.export(path_output, format="wav")

# ===== Login Suara =====
def login_dengan_suara():
    recognizer = sr.Recognizer()
    path_suara_login = "users/suara_login.wav"
    path_suara_login_trimmed = "users/suara_login_trimmed.wav"

    if not os.path.exists(path_suara_login):
        return False, "❌ File suara login tidak ditemukan"

    # Potong bagian sunyi dari file login
    potong_sunyi(path_suara_login, path_suara_login_trimmed)

    try:
        with sr.AudioFile(path_suara_login_trimmed) as source:
            audio_login = recognizer.record(source)
            hasil_login = recognizer.recognize_google(audio_login, language="id-ID")
            print(f"🔒 Kata kunci login: {hasil_login}")
    except Exception as e:
        return False, f"❌ Gagal membaca suara login: {e}"

    # Tunggu input suara dari user
    st.info("🎤 Silakan ucapkan kata login Anda...")
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            st.write("⏳ Mendengarkan...")
            audio_user = recognizer.listen(source, timeout=5)
            hasil_user = recognizer.recognize_google(audio_user, language="id-ID")
            st.write(f"🗣️ Anda mengatakan: {hasil_user}")

            if hasil_user.lower() == hasil_login.lower():
                return True, "✅ Login suara berhasil"
            else:
                return False, "❌ Suara tidak cocok"
    except Exception as e:
        return False, f"❌ Gagal mengenali suara dari mikrofon: {e}"
