import streamlit as st

st.set_page_config(page_title="Gandulator", page_icon="🧮", layout="centered")

# --- Zero-Scroll Mobile CSS ---
st.markdown("""
<style>
    /* Hide top header bar completely */
    header[data-testid="stHeader"] {
        display: none !important;
    }
    
    /* Remove default padding from the whole app */
    .stApp {
        margin: 0 !important;
        padding: 0 !important;
    }
    .block-container {
        padding-top: 0.5rem !important;
        padding-bottom: 0.5rem !important;
        padding-left: 0.5rem !important;
        padding-right: 0.5rem !important;
        max-width: 360px !important;
        margin: 0 auto !important;
    }
    
    /* Compact title */
    .calc-title {
        font-size: 1.3rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 0.3rem;
    }

    /* Keep all 4 columns side-by-side */
    div[data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important;
        gap: 6px !important;
        margin-bottom: -10px !important; /* Tightens row-to-row spacing */
    }

    /* Force columns to scale evenly to 25% */
    div[data-testid="column"] {
        min-width: 0 !important;
        flex: 1 1 0px !important;
        width: 25% !important;
        padding: 0 !important;
    }

    /* Compact button height for mobile screens */
    div.stButton > button {
        height: 2.6rem !important;
        width: 100% !important;
        font-size: 1.15rem !important;
        font-weight: 600 !important;
        border-radius: 8px !important;
        padding: 0 !important;
    }

    /* Compact display screen */
    div[data-baseweb="input"] input {
        font-size: 1.6rem !important;
        text-align: right !important;
        font-weight: bold !important;
        height: 2.8rem !important;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="calc-title">🧮 Gandulator</div>', unsafe_allow_html=True)

# State management
if "expression" not in st.session_state:
    st.session_state.expression = ""

def click(val):
    st.session_state.expression += str(val)

def clear():
    st.session_state.expression = ""

def calculate():
    try:
        st.session_state.expression = str(eval(st.session_state.expression))
    except ZeroDivisionError:
        st.session_state.expression = "Error: Div/0"
    except Exception:
        st.session_state.expression = "Error"

# Screen display
st.text_input("Screen", value=st.session_state.expression, label_visibility="collapsed", disabled=True)

# Grid layout
grid = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
]

for row in grid:
    cols = st.columns(4, gap="small", wrap=False)
    for i, val in enumerate(row):
        if val == "=":
            cols[i].button(val, on_click=calculate, use_container_width=True, type="primary")
        else:
            cols[i].button(val, on_click=click, args=(val,), use_container_width=True)

# Clear button
st.button("Clear (C)", on_click=clear, use_container_width=True)
