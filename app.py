import streamlit as st

# Page setup
st.set_page_config(page_title="Gandulator", page_icon="🧮", layout="centered")

st.title("🧮 Gandulator")
st.caption("A simple mobile-friendly web calculator")

# State management for inputs
if "expression" not in st.session_state:
    st.session_state.expression = ""

def click(val):
    st.session_state.expression += str(val)

def clear():
    st.session_state.expression = ""

def calculate():
    try:
        # Evaluate arithmetic expression safely
        st.session_state.expression = str(eval(st.session_state.expression))
    except ZeroDivisionError:
        st.session_state.expression = "Error: Div/0"
    except Exception:
        st.session_state.expression = "Error"

# Display Screen
st.text_input("Screen", value=st.session_state.expression, disabled=True)

# Grid Layout for Buttons
grid = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
]

for row in grid:
    cols = st.columns(4)
    for i, val in enumerate(row):
        if val == "=":
            cols[i].button(val, on_click=calculate, use_container_width=True)
        else:
            cols[i].button(val, on_click=click, args=(val,), use_container_width=True)

# Clear button spanning the width
st.button("Clear (C)", on_click=clear, use_container_width=True)
