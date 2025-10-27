import streamlit as st

# Title
st.title("🧮 Simple Streamlit Calculator")

# Description
st.write("A basic calculator built with Streamlit!")

# Input fields
num1 = st.number_input("Enter first number:", step=1.0)
num2 = st.number_input("Enter second number:", step=1.0)

# Operation selection
operation = st.selectbox(
    "Choose an operation:",
    ("Addition", "Subtraction", "Multiplication", "Division")
)

# Perform calculation
result = None
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("Cannot divide by zero!")

# Show result
if result is not None:
    st.success(f"Result: {result}")
