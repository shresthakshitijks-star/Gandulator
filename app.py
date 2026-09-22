import streamlit as st

st.set_page_config(page_title="Gandulator", page_icon="🧮", layout="centered")

# --- Custom CSS for Mobile Styling ---
st.markdown("""
<style>
    /* Clean up extra space on top */
    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 2rem;
        max-width: 420px;
    }
    /* Style calculator buttons */
    div.stButton > button {
        height: 3.2rem;
        font-size: 1.25rem;
        font-weight: 600;
        border-radius: 10px;
    }
    /* Style display box */
    div[data-baseweb="input"] input {
        font-size: 1.8rem !important;
        text-align: right;
        font-weight: bold;
        letter-spacing: 1px;
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

# Keypad grid layout
grid = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
]

# wrap=False prevents vertical stacking on mobile screens
for row in grid:
    cols = st.columns(4, gap="small", wrap=False)
    for i, val in enumerate(row):
        if val == "=":
            cols[i].button(val, on_click=calculate, use_container_width=True, type="primary")
        else:
            cols[i].button(val, on_click=click, args=(val,), use_container_width=True)

# Wide Clear button
st.button("Clear (C)", on_click=clear, use_container_width=True)
