import streamlit as st

st.title("Hello App")

#Take user Input

name = st.text_input("What's Your Name:")
age = int(st.number_input("What's Your Age:",  step=1, format="%d"))
city = st.text_input ("City:")

if name and age and city:
    st.success(f"Hello {name}! You're {age} years old and live in {city}.")

#Calculator Menue

st.header("Simple Calculator")

num1 = int(st.number_input("Enter First Number:", value=0.0))
num2 = int(st.number_input("Enter Second Number:", value=0.0))

operation = st.selectbox("Choose Option:", ["Add", "Subtract", "Multiplication", "Divide"])

result = None

if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Cannot divide by zero"

if result is not None:
    st.subheader(f"Result: {int(result)}")

