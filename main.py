import streamlit as st

# Title of the app
st.title("GenVoice by Sane")

# Instructions
st.write("Paste your numbers below (one per line or space-separated):")

# Text area for user input
input_data = st.text_area("Input", height=150)

# Button to trigger formatting
if st.button("Format"):
    if input_data.strip():  # Check if input is not empty
        # Split the input into individual numbers
        numbers = input_data.split()
        
        # Join the numbers with ", " as the separator
        output_data = ",".join(numbers)
        
        # Display the formatted output
        st.write("Formatted Output:")
        st.code(output_data)
    else:
        st.warning("Please paste some numbers before formatting.")