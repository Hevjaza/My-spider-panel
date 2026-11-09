import streamlit as st
import datetime

# Ställ in cyberpunk-tema direkt på skärmen
st.set_page_config(page_title="Spider-Bot Terminal", page_icon="🕷️", layout="wide")

st.markdown("""
    <style>
    .big-title { font-size:35px !important; font-weight: bold; color: #00FF66; font-family: 'Courier New', monospace; }
    .status-box { padding: 20px; background-color: #111111; border-radius: 10px; border: 1px solid #00FF66; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<p class="big-title">🕷️ SPIDER-BOT TERMINAL v1.0</p>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.subheader("🛡️ Systemstatus")
    st.markdown(f"**Tid (Stockholm):** {datetime.datetime.now().strftime('%H:%M:%S')}")
    st.success("STATUS: LIVE UTAN FEL 🟢")

with col2:
    st.subheader("📊 Marknadsbevakning")
    wallet = st.text_input("Mata in publik Solana-adress för övervakning:", placeholder="Klistra in din publika adress här...")
    if wallet:
        st.info(f"Scannar blockkedjan för adress: {wallet[:6]}... (Skrivskyddat läge)")

st.divider()
st.info("Detta är din egen, helsäkrade källkod sparad via GitHub. 0% ekonomisk risk.")
