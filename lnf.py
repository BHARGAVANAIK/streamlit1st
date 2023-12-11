import streamlit as st

def find_largest(num1, num2, num3):
    # Find the largest number
    largest = max(num1, num2, num3)
    return largest

# Streamlit app
st.title('Find the Largest Number')

# Input for three numbers
num1 = st.number_input('Enter the first number:', value=0)
num2 = st.number_input('Enter the second number:', value=0)
num3 = st.number_input('Enter the third number:', value=0)

# Button to find the largest number
if st.button('Find Largest'):
    largest_number = find_largest(num1, num2, num3)
    st.success(f'The largest number is: {largest_number}')
