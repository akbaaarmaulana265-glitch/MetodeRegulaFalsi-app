import streamlit as st
import time
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Regula Falsi • Dark Mode",
    page_icon="🌙",
    layout="wide"
)

# ---------------- CSS ----------------
st.markdown("""
<style>
    body {
        background-color: #0A0F1F;
        color: #E0E0E0;
        font-family: 'Segoe UI', sans-serif;
    }

    .title {
        text-align:center;
        font-size: 50px;
        font-weight: 900;
        background: linear-gradient(90deg, #00eaff, #005eff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 5px;
        animation: glow 2s infinite alternate;
    }

    @keyframes glow {
        from { text-shadow: 0 0 10px #00eaff; }
        to   { text-shadow: 0 0 25px #009dff; }
    }

    .card {
        padding: 25px;
        border-radius: 20px;
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(8px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.6);
        animation: fade 0.7s ease;
    }

    .result-card {
        padding: 18px;
        border-radius: 12px;
        background: rgba(0, 255, 170, 0.1);
        border-left: 6px solid #00ffaa;
        font-size: 20px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>🌙 Regula Falsi Calculator – Dark Mode</div>", unsafe_allow_html=True)
st.write("")

# ---------------- SIDEBAR ----------------
st.sidebar.title("📘 Quick Info")
st.sidebar.write("""
Metode **Regula Falsi** digunakan untuk mencari akar dari persamaan non-linear.
""")

# ----------- INPUT AREA -------------
col1, col2 = st.columns([1.2, 1])

with col1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("🔧 Input Parameter")

    fungsi = st.text_input("Masukkan Fungsi f(x):", "x**3 - x - 2")
    a = st.number_input("Batas bawah (a):", value=1.0)
    b = st.number_input("Batas atas (b):", value=2.0)
    toleransi = st.number_input("Toleransi error:", value=0.0001)

    tombol = st.button("⚡ Hitung Akar", use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("📑 Penjelasan Metode")
    st.write("""
Metode ini menggunakan garis secant antara titik (a, f(a)) dan (b, f(b)) untuk 
mendapatkan titik potong (akar perkiraan) sampai error kecil.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

def f(x):
    try:
        return eval(fungsi, {"x": x})
    except:
        return float("nan")

# Kolom Output
colR1, colR2 = st.columns(2)

# ----------- Proses Perhitungan -----------
data = []

if tombol:
    iterasi = 0

    while True:
        fa = f(a)
        fb = f(b)
        c = (a*fb - b*fa) / (fb - fa)
        fc = f(c)

        iterasi += 1

        data.append([iterasi, a, b, c, fa, fb, fc])

        if abs(fc) < toleransi:
            akar = c
            break

        if fa * fc < 0:
            b = c
        else:
            a = c

    df = pd.DataFrame(data, columns=["Iterasi", "a", "b", "c", "f(a)", "f(b)", "f(c)"])

    # ---------- OUTPUT ----------
    with colR1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("📊 Tabel Iterasi")
        st.dataframe(df, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with colR2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("📈 Grafik Konvergensi")

        fig, ax = plt.subplots()
        ax.plot(df["Iterasi"], df["c"], marker="o")
        ax.set_xlabel("Iterasi")
        ax.set_ylabel("Nilai c (akar perkiraan)")
        ax.set_title("Konvergensi Regula Falsi")
        st.pyplot(fig, clear_figure=True)

        st.markdown("</div>", unsafe_allow_html=True)

else:
    with colR1:
        st.info("Tabel akan muncul setelah perhitungan.")
    with colR2:
        st.info("Grafik akan muncul setelah perhitungan.")
