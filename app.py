import streamlit as st
from datetime import datetime, date, time, timedelta
from urllib.parse import quote
from PIL import Image

st.set_page_config(page_title="WhatsApp Daily Task Report Tool", page_icon="📋", layout="centered")

try:
    logo = Image.open("logo.png")
    st.image(logo, width=150)
except Exception as e:
    st.warning(f"Logo could not be loaded: {e}")
    
st.title("📋 WhatsApp Daily Task Report Tool")
st.markdown("Create a professional daily task report and send it directly on WhatsApp.")

# ---------- Helpers ----------
def calculate_total_time(in_time: time, out_time: time, lunch_minutes: int) -> timedelta:
    start_dt = datetime.combine(date.today(), in_time)
    end_dt = datetime.combine(date.today(), out_time)

    # Handle overnight shift if out-time is earlier than in-time
    if end_dt < start_dt:
        end_dt += timedelta(days=1)

    total = end_dt - start_dt - timedelta(minutes=lunch_minutes)
    return total if total.total_seconds() > 0 else timedelta(0)


def format_timedelta(td: timedelta) -> str:
    total_seconds = int(td.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    return f"{hours}h {minutes}m"


# ---------- Form ----------
with st.form("daily_report_form"):
    st.subheader("Enter Daily Report Details")

    report_date = st.date_input("Date", value=date.today())
    name = st.text_input("Name", placeholder="Enter your full name")
    task_performed = st.text_area(
        "Task Performed",
        placeholder="Example:\n- Completed API integration\n- Fixed login bug\n- Tested Streamlit UI",
        height=180,
    )

    col1, col2 = st.columns(2)
    with col1:
        in_time = st.time_input("In-Time", value=time(9, 0))
    with col2:
        out_time = st.time_input("Out-Time", value=time(18, 0))

    lunch_break = st.number_input("Lunch Break (minutes)", min_value=0, max_value=180, value=60, step=5)

    phone_number = st.text_input(
        "WhatsApp Number (with country code, no +)",
        placeholder="Example: 919876543210",
    )

    submitted = st.form_submit_button("Generate WhatsApp Message")

# ---------- Output ----------
if submitted:
    if not name.strip():
        st.error("Please enter your name.")
    elif not task_performed.strip():
        st.error("Please enter the task performed.")
    else:
        total_time = calculate_total_time(in_time, out_time, lunch_break)
        total_time_str = format_timedelta(total_time)

        message = f"""📅 *Daily Task Report*\n\nDate: {report_date.strftime('%d-%m-%Y')}\nName: {name}\nTask Performed:\n{task_performed}\n\nIn-Time: {in_time.strftime('%I:%M %p')}\nLunch Break: {lunch_break} minutes\nOut-Time: {out_time.strftime('%I:%M %p')}\nTotal Time: {total_time_str}\n"""

        st.success("Message generated successfully!")
        st.subheader("📨 WhatsApp Message Preview")
        st.code(message, language="text")

        st.subheader("📌 Copy Message")
        st.text_area("Copy this message", value=message, height=250)

        # WhatsApp link
        encoded_message = quote(message)
        if phone_number.strip():
            whatsapp_url = f"https://wa.me/{phone_number}?text={encoded_message}"
            st.link_button("🚀 Send on WhatsApp", whatsapp_url)
        else:
            st.info("Enter a WhatsApp number to enable the direct send button.")

# ---------- Footer ----------
st.markdown("---")
st.caption("Built with Python + Streamlit for quick daily reporting.")
