import streamlit as st

st.title("Metode Regula Falsi")
st.write(
    "Selamat Datang Di Layanan Kami https://www.instagram.com/?utm_source=pwa_homescreen&__pwa=1"
)
if fa * fc < 0:
b = c
else:
a = c


iterasi += 1
if iterasi > 100:
akar = None
break



with colR1:
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("### ✅ Hasil Perhitungan")


if akar is not None:
st.markdown(f"<div class='result'>Akar ditemukan pada:<br><b>{akar}</b></div>", unsafe_allow_html=True)
else:
st.error("Akar tidak ditemukan dalam 100 iterasi.")


st.markdown("</div>", unsafe_allow_html=True)



df = pd.DataFrame(data, columns=["Iterasi", "a", "b", "c", "f(a)", "f(b)", "f(c)"])


with colR1:
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("### 📊 Tabel Iterasi")
st.dataframe(df, use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)



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


st.markdown("<div class='footer'>Dibuat dengan ❤️ menggunakan Streamlit • Regula Falsi Professional Edition</div>", unsafe_allow_html
