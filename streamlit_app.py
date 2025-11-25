import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from math import *


# ================================
# ⚡ PROFESSIONAL UI STYLING
# ================================
st.set_page_config(page_title="Regula Falsi Calculator", layout="wide", page_icon="⚡")


# Custom CSS
st.markdown(
"""
<style>
body { background-color: #f5f7fa; }
.title {
text-align: center;
font-size: 42px;
color: #2b5876;
font-weight: bold;
}
.subtitle {
text-align: center;
font-size: 20px;
color: #4a6572;
}
.card {
padding: 20px;
border-radius: 20px;
background: white;
box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
}
.result {
padding: 15px;
border-radius: 10px;
background-color: #e8f5e9;
color: #1b5e20;
font-size: 20px;
}
.footer {
margin-top: 30px;
text-align: center;
color: #7b8794;
}
</style>
""",
unsafe_allow_html=True
)

# ================================
"Metode *Regula Falsi* (False Position) menggunakan garis sekant untuk memperkirakan akar persamaan f(x)."
)
st.write("""
**Kelebihan:**
- Lebih stabil dibanding metode sekant
- Tidak memerlukan turunan f(x)


**Kekurangan:**
- Lebih lambat dibanding Newton-Raphson
- Bisa stagnan pada beberapa kasus
""")
st.markdown("</div>", unsafe_allow_html=True)


# ================================
# FUNCTION
# ================================
def f(x):
return eval(fungsi)


# ================================
# PROCESSING LOGIC
# ================================
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

# ================================
# RESULT DISPLAY
# ================================
with colR1:
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("### ✅ Hasil Perhitungan")


if akar is not None:
st.markdown(f"<div class='result'>Akar ditemukan pada:<br><b>{akar}</b></div>", unsafe_allow_html=True)
else:
st.error("Akar tidak ditemukan dalam 100 iterasi.")


st.markdown("</div>", unsafe_allow_html=True)


# ================================
# TABLE
# ================================
df = pd.DataFrame(data, columns=["Iterasi", "a", "b", "c", "f(a)", "f(b)", "f(c)"])


with colR1:
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("### 📊 Tabel Iterasi")
st.dataframe(df, use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)


# ================================
# GRAPH
# ================================
with colR2:
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("### 📈 Grafik Konvergensi Akar")


plt.figure()
plt.plot(df["Iterasi"], df["c"], marker="o")
plt.xlabel("Iterasi")
plt.ylabel("Nilai c (perkiraan akar)")
plt.title("Grafik Konvergensi Metode Regula Falsi")
st.pyplot(plt, clear_figure=True)


st.markdown("</div>", unsafe_allow_html=True)


# ================================
# FOOTER
# ================================
st.markdown("<div class='footer'>Dibuat dengan ❤️ menggunakan Streamlit • Regula Falsi Professional Edition</div>", unsafe_allow_html=True)


# --- DARK MODE & DASHBOARD VERSION BELOW WILL BE ADDED ---
