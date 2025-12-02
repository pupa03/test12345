import streamlit as st
import pandas as pd
import google.generativeai as genai
from navbar import navbar
# api_key=st.secrets["GEMINI_API_KEY"]
# st.write(api_key)

# st.set_page_config(page_title="Plotting Demo", page_icon="📈")
# st.markdown("# Plotting Demo")
# st.sidebar.header("Plotting Demo")

def wide_space_default():
    st.set_page_config(layout="wide")
                       
wide_space_default()


navbar()
# _______________


st.header('Page 1 Hello')
st.page_link("app.py", label="Back", icon="1️⃣")

# _______________

if "selected_df" not in st.session_state:
    st.error("ยังไม่มีข้อมูลจากหน้าแรก กรุณาเลือกก่อน")
    st.stop()

selected_df = st.session_state.selected_df

st.write("### หุ้นที่คุณเลือก")
st.dataframe(selected_df)

# _______________
# VDO
# img -> link

#test youtube podcast tiktok
st.markdown('VDO test .mp3')
# video_file = open("YT03042025_CH3.mp3", "rb")
# video_bytes = video_file.read()
# st.video(video_bytes)

# Youtube
VIDEO_URL = "https://youtu.be/bqhcJS8xrJY?si=v-BZETooLRtJi4Mm"
# VIDEO_URL = "https://vt.tiktok.com/ZSfVQGU2v/"
st.video(VIDEO_URL)

# _______________
# LLM

st.markdown('test LLM')
# records = selected_df.to_dict(orient="records")

names = selected_df["Name"].tolist()
# st.write(names)

prompt = f"""
จากข้อมูลชุดนี้: {names}
ช่วยแนะนำ portfolio ให้หน่อย
ขอ 2 - 3 บรรทัด
"""

st.write("### Prompt")
st.code(prompt)

# ________________
# CALL GEMINI

# save session?
genai.configure(api_key=st.secrets["GEMINI_API_KEY"]) 

if st.button("Generate Summary"):
    
    model = genai.GenerativeModel("gemini-2.5-flash")

    response = model.generate_content(prompt)

    st.write("### ผลลัพธ์จาก Gemini")
    st.write(response.text)

