import streamlit as st

st.title("🧮 Simple Calculator")

num1 = st.number_input("Enter First Number")

num2 = st.number_input("Enter Second Number")

operation = st.selectbox(
    "Choose Operation",
    ["Addition", "Subtraction", "Multiplication", "Division"]
)

if st.button("Calculate"):

    if operation == "Addition":
        result = num1 + num2
        st.success(f"Answer: {result}")

    elif operation == "Subtraction":
        result = num1 - num2
        st.success(f"Answer: {result}")

    elif operation == "Multiplication":
        result = num1 * num2
        st.success(f"Answer: {result}")

    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
            st.success(f"Answer: {result}")
        else:
            st.error("Cannot divide by zero")