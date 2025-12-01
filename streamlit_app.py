import streamlit as st

st.set_page_config(page_title="Regula Falsi Calculator", layout="wide", page_icon="⚡")

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
""", unsafe_allow_html=True)st.markdown("<div class='title'>⚡ Metode Regula Falsi </div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Web Sederhana Regula Falsi</div>", unsafe_allow_html=True)


st.write("---")

col1, col2 = st.columns([1.2, 1])

with col1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### 🔧 Input Parameter")


    fungsi = st.text_input("Masukkan Fungsi f(x):", "x**3 - x - 2")
    a = st.number_input("Batas bawah (a):", value=1.0)
    b = st.number_input("Batas atas (b):", value=2.0)
    toleransi = st.number_input("Toleransi error:", value=0.0001)


    hitung = st.button("🔍 Hitung Akar", use_container_width=True)


    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### ℹ Informasi Metode")
    st.write(
        "Metode Regula Falsi (False Position) menggunakan garis sekant untuk memperkirakan akar persamaan f(x)."
    )
    st.write("""
    *Kelebihan:*
    - Lebih stabil dibanding metode sekant
    - Tidak memerlukan turunan f(x)


    *Kekurangan:*
    - Lebih lambat dibanding Newton-Raphson
    - Bisa stagnan pada beberapa kasus
    """)
    st.markdown("</div>", unsafe_allow_html=True)
    
def f(x):
    return eval(fungsi)

if hitung:
    st.write("---")


    colR1, colR2 = st.columns([1.2, 1])


    iterasi = 0
    data = []


    while True:
        fa = f(a)
        fb = f(b)
        c = b - (fb * (b - a)) / (fb - fa)
        fc = f(c)
        
        data.append([iterasi, a, b, c, fa, fb, fc])

        if abs(fc) < toleransi:
            akar = c
            break
            
        if fa * fc < 0:
            b = c
        else:
            a = c
            
        iterasi += 1
        if iterasi > 100:
            akar = None
            break

colR1, colR2 = st.columns(2)

akar = None
data = []

if hitung:  
    
    a_local = a
    b_local = b

    iterasi = 0
    data = []
    
    while True:
        fa = f(a_local)
        fb = f(b_local)

        denom = (fb - fa)
        if denom == 0:
            akar = None
            break

        c = b_local - fb * (b_local - a_local) / denom
        fc = f(c)

        data.append([iterasi, a_local, b_local, c, fa, fb, fc])

        if abs(fc) < toleransi:
            akar = c
            break

        if fa * fc < 0:
            b_local = c
        else:
            a_local = c

        iterasi += 1
        if iterasi > 100:
            akar = None
            break

with colR1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### ✅ Hasil Perhitungan")

    if akar is not None:
        st.markdown(
            f"<div class='result'>Akar ditemukan pada:<br><b>{akar}</b></div>",
            unsafe_allow_html=True
        )
    else:
        if hitung:
            st.error("Akar tidak ditemukan dalam 100 iterasi atau interval tidak valid.")
        else:
            st.info("Tekan tombol 'Hitung Akar' untuk memulai perhitungan.")

    st.markdown("</div>", unsafe_allow_html=True)


data = []
if data:
    df = pd.DataFrame(data, columns=["Iterasi", "a", "b", "c", "f(a)", "f(b)", "f(c)"])
    
    
    with colR1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### 📊 Tabel Iterasi")
        st.dataframe(df, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
       
    with colR2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### 📈 Grafik Konvergensi Akar")
        
        fig, ax = plt.subplots()
        ax.plot(df["Iterasi"], df["c"], marker="o")
        ax.set_xlabel("Iterasi")
        ax.set_ylabel("Nilai c (perkiraan akar)")
        ax.set_title("Grafik Konvergensi Metode Regula Falsi")
        st.pyplot(fig, clear_figure=True)
        
        st.markdown("</div>", unsafe_allow_html=True)

else:
    with colR1:
        st.info("Tabel iterasi akan muncul setelah perhitungan selesai.")
    with colR2:
        st.info("Grafik konvergensi akan muncul setelah perhitungan selesai.")

st.markdown("<div class='footer'>Dibuat oleh Akbar Maulana ❤ menggunakan Streamlit • Regula Falsi </div>", unsafe_allow_html=True)

# --- DARK MODE & DASHBOARD VERSION BELOW WILL BE ADDED ---
