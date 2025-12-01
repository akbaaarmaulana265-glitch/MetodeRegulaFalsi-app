import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import time

# -----------------------------------------
#            DARK MODE CUSTOM CSS
# -----------------------------------------
st.markdown("""
<style>
body {
    background-color: #0A0F1F;
    color: #e0e0e0;
}
h1, h2, h3, h4, h5, h6 {
    color: #00eaff;
}
.card {
    background: #111a33;
    padding: 20px;
    border-radius: 12px;
    margin-top: 10px;
    box-shadow: 0px 0px 10px #00eaff33;
}
.result {
    color: #00ffcc;
    font-size: 20px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------------------
#              TITLE APP
# -----------------------------------------
st.title("📘 Aplikasi Metode Regula Falsi — Versi Streamlit (Dark Mode + Plotly)")

st.write("Masukkan fungsi, batas bawah, batas atas, dan toleransi.")

# -----------------------------------------
#              INPUT USER
# -----------------------------------------
fungsi_input = st.text_input("Fungsi f(x) :", "x**3 - x - 2")
a = st.number_input("Batas bawah (a) :", value=1.0)
b = st.number_input("Batas atas (b) :", value=2.0)
tol = st.number_input("Toleransi :", value=0.0001)

# -----------------------------------------
#         DEFINISI FUNGSI DINAMIS
# -----------------------------------------
def f(x):
    try:
        return eval(fungsi_input, {"x": x, "np": np})
    except Exception:
        return None

# -----------------------------------------
#           TOMBOL PROSES
# -----------------------------------------
if st.button("Hitung Regula Falsi"):
    with st.spinner("Menghitung..."):
        time.sleep(0.5)

    iterasi_list = []
    c_list = []

    fa = f(a)
    fb = f(b)

    if fa is None or fb is None:
        st.error("❌ Fungsi tidak valid. Periksa input fungsi!")
    elif fa * fb > 0:
        st.error("❌ f(a) dan f(b) harus berlawanan tanda (akar terletak di antara a dan b).")
    else:
        # -----------------------------------------
        #           PERHITUNGAN REGULA FALSI
        # -----------------------------------------
        iterasi = 0
        while True:
            iterasi += 1
            c = (a * f(b) - b * f(a)) / (f(b) - f(a))
            fc = f(c)

            iterasi_list.append(iterasi)
            c_list.append(c)

            if abs(fc) < tol:
                break

            if f(a) * fc < 0:
                b = c
            else:
                a = c

            if iterasi >= 50:
                break

        akar = c

        # -----------------------------------------
        #           TAMPILKAN HASIL
        # -----------------------------------------
        col1, col2 = st.columns(2)

        # ========= Kolom Hasil ==========
        with col1:
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.subheader("📌 Hasil Perhitungan")
            st.write(f"**Akar ditemukan:** `{akar}`")
            st.write(f"Jumlah Iterasi: **{iterasi}**")
            st.markdown("</div>", unsafe_allow_html=True)

        # ========= Kolom Grafik Plotly ==========
        with col2:
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.subheader("📈 Grafik Konvergensi")

            fig = go.Figure()
            fig.add_trace(go.Scatter(
                x=iterasi_list,
                y=c_list,
                mode="lines+markers",
                line=dict(width=3),
                marker=dict(size=7)
            ))

            fig.update_layout(
                template="plotly_dark",
                xaxis_title="Iterasi",
                yaxis_title="Nilai c",
                title="Grafik Konvergensi Metode Regula Falsi",
                plot_bgcolor="#0A0F1F",
                paper_bgcolor="#0A0F1F",
                font=dict(color="#e0e0e0")
            )

            st.plotly_chart(fig, use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

        # -----------------------------------------
        #           TABEL ITERASI
        # -----------------------------------------
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("📊 Tabel Iterasi")

        df = pd.DataFrame({
            "Iterasi": iterasi_list,
            "c": c_list
        })

        st.dataframe(df, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
