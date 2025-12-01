import streamlit as st
import time

st.set_page_config(
    page_title="Regula Falsi • Dark Mode",
    page_icon="🌙",
    layout="wide"
)

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

    @keyframes fade {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0px); }
    }

    .result-card {
        padding: 18px;
        border-radius: 12px;
        background: rgba(0, 255, 170, 0.1);
        border-left: 6px solid #00ffaa;
        animation: fade 0.6s ease;
        font-size: 20px;
    }

    .sidebar .sidebar-content {
        background-color: #0D1326;
        color: white;
    }

    .small-text {
        font-size: 12px;
        opacity: 0.7;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>🌙 Regula Falsi Calculator – Dark Mode</div>", unsafe_allow_html=True)
st.write("")

st.sidebar.title("📘 Quick Info")
st.sidebar.write("""
**Regula Falsi** adalah metode akar numerik menggunakan pendekatan *secant* tetapi menjaga interval tetap valid.

**Dipakai untuk:**
- Persamaan non-linear  
- Estimasi akar tanpa turunan  
""")

st.sidebar.write("---")
st.sidebar.markdown(
    "<div class='small-text'>Dark Mode UI by Akbar Maulana</div>",
    unsafe_allow_html=True
)

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
Metode **Regula Falsi** bekerja dengan:
1. Menghitung garis secant antara titik (a, f(a)) dan (b, f(b))
2. Menemukan titik potong garis → perkiraan akar
3. Memperbarui interval berdasarkan tanda f(c)
4. Mengulang sampai akurasi tercapai
    """)
    st.markdown("</div>", unsafe_allow_html=True)

def f(x):
    return eval(fungsi)

data = []
if tombol:

    with st.spinner("Menghitung akar... 🔄"):
        time.sleep(0.8)

    a_local, b_local = a, b
    data = []
    akar = None

    for i in range(100):
        fa = f(a_local)
        fb = f(b_local)

        if fb - fa == 0:
            break

        c = b_local - fb * (b_local - a_local) / (fb - fa)
        fc = f(c)

        data.append([i, a_local, b_local, c, fa, fb, fc])

        if abs(fc) < toleransi:
            akar = c
            break

        if fa * fc < 0:
            b_local = c
        else:
            a_local = c

    st.write("---")
    colR1, colR2 = st.columns([1.1, 1])

    with colR1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("📌 Hasil Perhitungan")

        if akar is not None:
            st.markdown(
                f"<div class='result-card'>Akar ditemukan pada:<br><b>{akar}</b></div>",
                unsafe_allow_html=True
            )
            st.success("Perhitungan selesai ✔")
        else:
            st.error("Akar tidak ditemukan atau interval tidak sesuai.")

        st.markdown("</div>", unsafe_allow_html=True)

    df = pd.DataFrame(
        data,
        columns=["Iterasi", "a", "b", "c", "f(a)", "f(b)", "f(c)"]
    )
    
    with colR1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("📊 Tabel Iterasi")
        st.dataframe(df, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with colR2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("📈 Grafik Konvergensi")

        fig, ax = plt.subplots()
        ax.plot(df["Iterasi"], df["c"], marker="o", linewidth=2, color="#00eaff")
        ax.set_facecolor("#0D1326")
        fig.patch.set_facecolor("#0A0F1F")

        ax.set_xlabel("Iterasi", color="white")
        ax.set_ylabel("Nilai c", color="white")
        ax.set_title("Pergerakan Akar", color="#00eaff")

        ax.tick_params(colors="white")

        st.pyplot(fig)
        st.markdown("</div>", unsafe_allow_html=True)

else:
    st.info("Klik tombol **Hitung Akar** untuk memulai perhitungan.")
