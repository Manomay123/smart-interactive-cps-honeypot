import streamlit as st
import pandas as pd

st.set_page_config(page_title="CPS Honeypot Dashboard", layout="wide")
st.title("🛡️ Cyber-Physical Systems (CPS) Honeypot Dashboard")

df = pd.DataFrame([
    {"timestamp": "2026-08-14T10:00:00Z", "src_ip": "192.168.1.105", "service": "Modbus/TCP", "attack_type": "Modbus Protocol Manipulation"},
    {"timestamp": "2026-08-14T10:15:00Z", "src_ip": "10.0.0.42", "service": "MQTT", "attack_type": "Unauthorized Connect"},
    {"timestamp": "2026-08-14T10:30:00Z", "src_ip": "172.16.0.8", "service": "HTTP", "attack_type": "Command Injection"},
    {"timestamp": "2026-08-14T10:45:00Z", "src_ip": "192.168.1.105", "service": "SSH", "attack_type": "Brute Force"}
])

col1, col2, col3 = st.columns(3)
col1.metric("Total Events", len(df))
col2.metric("Targeted Services", df['service'].nunique())
col3.metric("Unique Attacker IPs", df['src_ip'].nunique())

st.divider()
c1, c2 = st.columns(2)
with c1:
    st.subheader("Attacks by Service")
    st.bar_chart(df['service'].value_counts())
with c2:
    st.subheader("Attack Vectors Identified")
    st.bar_chart(df['attack_type'].value_counts())

st.subheader("📋 Detailed Incident Log")
st.dataframe(df, use_container_width=True)