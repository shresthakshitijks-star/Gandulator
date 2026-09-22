import streamlit as st

st.set_page_config(page_title="Gandulator", page_icon="🧮", layout="centered")

# --- Custom Styling for PC & Mobile ---
st.markdown("""
<style>
    /* Remove padding around main container */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 1rem !important;
        padding-left: 0.5rem !important;
        padding-right: 0.5rem !important;
        max-width: 380px !important;
        margin: 0 auto !important;
    }

    /* Keep all 4 columns in a single row without horizontal overflow */
    div[data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important;
        gap: 6px !important;
        width: 100% !important;
    }

    /* Force columns to scale evenly to exactly 25% */
    div[data-testid="column"] {
        min-width: 0 !important;
        flex: 1 1 0px !important;
        width: 25% !important;
        padding: 0 !important;
    }

    /* Touchscreen button dimensions */
    div.stButton > button {
        height: 3.2rem !important;
        width: 100% !important;
        font-size: 1.25rem !important;
        font-weight: 600 !important;
        border-radius: 8px !important;
        padding: 0 !important;
    }

    /* Screen display styling */
    div[data-baseweb="input"] input {
        font-size: 1.8rem !important;
        text-align: right !important;
        font-weight: bold !important;
        height: 3.2rem !important;
    }
</style>
""", unsafe_allow_html=True)

st.title("🧮 Gandulator")

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

# Display screen
st.text_input("Screen", value=st.session_state.expression, label_visibility="collapsed", disabled=True)

# Keypad layout
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

# Wide Clear button
st.button("Clear (C)", on_click=clear, use_container_width=True)
