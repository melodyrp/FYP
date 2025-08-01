import streamlit as st
import time
import os
import re
import streamlit.components.v1 as components

# === CONFIG ===
LOG_FILE = "terminal_log.txt"
REFRESH_INTERVAL_SEC = 5

st.set_page_config(page_title="LLM Security Monitor", layout="wide")
st.title("🛡️ LLM Chatbot General Alert Dashboard")

auto_refresh = st.checkbox("🔁 Auto-refresh every 5 seconds", value=True)

# === DESKTOP NOTIFICATION ===
def show_desktop_notification(message):
    components.html(f"""
        <script>
        if (Notification.permission !== "granted") {{
            Notification.requestPermission();
        }}
        if (Notification.permission === "granted") {{
            new Notification("🚨 New LLM Alert", {{
                body: `{message}`,
            }});
        }}
        </script>
    """, height=0)

# === SESSION STATE ===
if "log_position" not in st.session_state:
    st.session_state.log_position = 0
if "alerts" not in st.session_state:
    st.session_state.alerts = []
if "latest_alert" not in st.session_state:
    st.session_state.latest_alert = ""

# === MATCH ALERT PATTERNS ===
def is_alert(entry: str) -> bool:
    entry_lower = entry.lower()
    keywords = [
        "blocked prompt injection attempt",
        "blocked jailbreak attempt",
        "blocked csv-style injection attempt",
        "blocked suspicious response",
        "blocked gpt leakage"
    ]
    return any(keyword in entry_lower for keyword in keywords)

# === READ NEW LOG ENTRIES ===
def read_new_alerts():
    new_alerts = []
    if not os.path.exists(LOG_FILE):
        return new_alerts

    with open(LOG_FILE, "r", encoding="utf-8") as f:
        f.seek(st.session_state.log_position)
        raw = f.read()
        st.session_state.log_position = f.tell()

    # Split log entries (even if multi-line)
    log_blocks = re.split(r'(?=\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\])', raw)

    for block in log_blocks:
        block = block.strip()
        if not block:
            continue
        if is_alert(block):
            new_alerts.append(block)
            st.session_state.latest_alert = block
            show_desktop_notification(block)

    return new_alerts

# === GET & STORE NEW ALERTS ===
new_alerts = read_new_alerts()
if new_alerts:
    st.session_state.alerts.extend(new_alerts)
    st.session_state.latest_alert = new_alerts[-1]

# === MOST RECENT ALERT ===
st.subheader("🚨 Most Recent Alert")
if st.session_state.latest_alert:
    st.error(st.session_state.latest_alert)
else:
    st.info("✅ No alerts yet.")

# === FULL ALERT LOG DISPLAY ===
st.markdown("### 📋 General Alert Feed")
if st.session_state.alerts:
    for alert in st.session_state.alerts[-50:]:
        st.markdown(f"""
        <div style='background-color:#f9f9f9; padding: 10px; border-radius: 5px;
                     overflow-x: auto; white-space: pre-wrap; font-family: monospace;
                     border: 1px solid #ccc; margin-bottom: 10px;'>
            {alert}
        </div>
        """, unsafe_allow_html=True)
else:
    st.info("No alerts recorded yet.")

# === METRIC ===
st.markdown("---")
st.metric("⚠️ Total Alerts", len(st.session_state.alerts))

# === AUTO REFRESH ===
if auto_refresh:
    time.sleep(REFRESH_INTERVAL_SEC)
    st.rerun()
