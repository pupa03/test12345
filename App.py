import streamlit as st
import pandas as pd
from navbar import navbar

# st.set_page_config(
#     page_title="Hello",
#     page_icon="👋",
# )
def wide_space_default():
    st.set_page_config(layout="wide")
                       
wide_space_default()

# ___________________
# Navigation Bar
# --- Init state ---
if "page" not in st.session_state:
    st.session_state["page"] = "Home"   # ตั้งค่าเริ่มต้น

navbar()
# # สร้าง Session State สำหรับเก็บข้อมูลร่วมกัน
# if 'shared_counter' not in st.session_state:
#     st.session_state['shared_counter'] = 0


# # ใช้ st.markdown เพื่อสร้างโครงสร้าง Navbar
# st.markdown('<div class="navbar-container">', unsafe_allow_html=True)
# st.markdown('<span class="navbar-brand">App Name</span>', unsafe_allow_html=True)

# # ใช้ st.columns เพื่อวางปุ่มนำทางในแถวเดียวกัน
# col1, col2, col3, col_spacer = st.columns([1, 1, 1, 10])

# with col1:
#     st.markdown('<div class="navbar-link-container">', unsafe_allow_html=True)
#     if st.button("Home", key="nav_home"):
#         st.switch_page("app.py") # ชี้ไปที่ไฟล์หลัก
#     st.markdown('</div>', unsafe_allow_html=True)

# with col2:
#     st.markdown('<div class="navbar-link-container">', unsafe_allow_html=True)
#     if st.button("Page 1", key="nav_page1"):
#         st.switch_page("pages/1_page1.py")
#     st.markdown('</div>', unsafe_allow_html=True)

# with col3:
#     st.markdown('<div class="navbar-link-container">', unsafe_allow_html=True)
#     if st.button("Page 2", key="nav_page2"):
#         st.switch_page("pages/2_page2.py")
#     st.markdown('</div>', unsafe_allow_html=True)

# st.markdown('</div>', unsafe_allow_html=True)
# ___________________


st.write("# Welcome to Streamlit! 👋")
# st.sidebar.success("Select a demo above.")

st.header('hello')
# ___________________
@st.cache_data
def load_data(df):
    df = pd.read_csv(df)
    return df

df = load_data('test1.csv')
st.write(df)
# ____________________

# --- ใช้ session_state เก็บสถานะการเลือก ---
if "selected_rows" not in st.session_state:
    st.session_state.selected_rows = set()

st.write("## กดเลือก")

# --- แสดงทีละรายการ ---
for i, row in df.iterrows():
    col1, col2 = st.columns([0.1, 0.9])

    # Checkbox
    checked = col1.checkbox(
        "",
        value=(i in st.session_state.selected_rows),
        key=f"cb_{i}"
    )

    # ถ้าเลือก → บันทึกสถานะ
    if checked:
        st.session_state.selected_rows.add(i)
    else:
        st.session_state.selected_rows.discard(i)

    # highlight ถ้าเลือก
    if i in st.session_state.selected_rows:
        col2.markdown(
            f"<div style='background-color:#D6EAF8;padding:8px;border-radius:6px;'>"
            f"{row['Name']}"
            f"</div>",
            unsafe_allow_html=True,
        )
    else:
        col2.markdown(
            f"<div style='padding:8px;'>"
            f"{row['Name']}"
            f"</div>",
            unsafe_allow_html=True,
        )

# --- ปุ่มยืนยัน ---
if st.button("ยืนยันตัวเลือก"):
    # เก็บ - ส่งไปหน้าอื่น
    selected_df = df.loc[list(st.session_state.selected_rows)]
    st.session_state.selected_df = selected_df
    st.success("คุณเลือกข้อมูลดังนี้:")
    st.dataframe(selected_df)

    # st.switch_page("pages/1_page1.py") # กดแล้วไป page2 เลย
    # selected_data = selected_df.to_dict(orient="records")

    names = selected_df["Name"].tolist()
    st.markdown(names)

st.page_link("pages/1_page1.py", label="Next", icon="1️⃣")
