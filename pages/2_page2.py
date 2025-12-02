import streamlit as st

def wide_space_default():
    st.set_page_config(layout="wide")
                       
wide_space_default()

st.markdown("## HELLO PAGE 2")

from navbar import navbar
if "page" not in st.session_state:
    st.session_state["page"] = "Home"
navbar()

st.title("สรุปข้อมูลแบบหัวข้อย่อย")

data = {
    "1. บทนำ": "เนื้อหาของบทนำ …",
    "2. วิธีการทำงาน": "อธิบายขั้นตอน …",
    "3. ผลลัพธ์": "รายละเอียดผลลัพธ์ …",
    "4. สรุปและข้อเสนอแนะ": "สรุปทั้งหมด …"
}

for title, content in data.items():
    with st.expander(title):
        st.write(content)
