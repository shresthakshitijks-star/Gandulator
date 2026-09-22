import streamlit as st

st.set_page_config(page_title="Gandulator", page_icon="🧮", layout="centered")

# --- Zero-Scroll Mobile CSS ---
st.markdown("""
<style>
    /* Prevent page scrolling completely */
    html, body, [data-testid="stAppViewContainer"], .main {
        overflow: hidden !important;
        height: 100vh !important;
        max-height: 100vh !important;
    }

    /* Hide top header bar, toolbar, and footer */
    header[data-testid="stHeader"], 
    div[data-testid="stToolbar"], 
    footer {
        display: none !important;
    }
    
    /* Minimize root app paddings */
    .stApp {
        margin: 0 !important;
        padding: 0 !important;
    }
    
    .block-container {
        padding-top: 0.5rem !important;
        padding-bottom: 0.2rem !important;
        padding-left: 0.75rem !important;
        padding-right: 0.75rem !important;
        max-width: 320px !important;
        margin: 0 auto !important;
    }

    /* Strip all vertical gaps injected by Streamlit */
    div[data-testid="stVerticalBlock"],
    div[data-testid="stVerticalBlockBorderWrapper"] {
        gap: 0.25rem !important;
    }

    div[data-testid="stElementContainer"] {
        margin: 0 !important;
        padding: 0 !important;
    }

    /* Compact title */
    .calc-title {
        font-size: 1.15rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 0.2rem;
    }

    /* Keep rows side-by-side with 0 row-wrap */
    div[data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important;
        gap: 6px !important;
        margin-bottom: 0 !important;
    }

    /* Force 4 equal columns on all screen widths */
    div[data-testid="column"] {
        min-width: 0 !important;
        flex: 1 1 0px !important;
        width: 25% !important;
        padding: 0 !important;
    }

    /* Button sizing and spacing */
    div.stButton {
        margin: 0 !important;
        padding: 0 !important;
    }

    div.stButton > button {
        height: 2.3rem !important;
        min-height: 2.3rem !important;
        width: 100% !important;
        font-size: 1.1rem !important;
        font-weight: 600 !important;
        border-radius: 8px !important;
        padding: 0 !important;
        margin: 0 !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }

    /* Compact display input */
    div[data-testid="stTextInput"] {
        margin-bottom: 0.2rem !important;
    }

    div[data-baseweb="input"] {
        height: 2.5rem !important;
        min-height: 2.5rem !important;
    }

    div[data-baseweb="input"] input {
        font-size: 1.5rem !important;
        text-align: right !important;
        font-weight: bold !important;
        height: 2.5rem !important;
        padding-right: 0.75rem !important;
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
