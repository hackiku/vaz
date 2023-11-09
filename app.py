import streamlit as st
import openai
# from dotenv import load_dotenv
# import os
# load_dotenv()
# openai.api_key = os.getenv('OPENAI_API_KEY')

# Load OpenAI API key
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Define gpt-4 outside of Streamlit instance
gpt_prompt = """you will act as a matlab to python refactoring machine. I will paste matlab code and you will just output the refactored code in python, including not too verbose but useful comments. Important: do not output anything beside the code — this is powering a refactoring app within an aerospace university research program via gpt-4 API. REQUIREMENTS: python 3.9, numpy, matplotlib, scipy, simpy, pandas. The code to refactor is: 
"""

# UI elements
st.title('MATLAB to Python Refactorer')
st.write('Paste MATLAB code and get Python equivalent refactored by GPT-4.')

# Sample MATLAB code for demonstration purposes
sample_matlab_code = """% Sample MATLAB code for CFD
rho = 1.225; density of air (kg/m^3)
mu = 1.7894e-5; dynamic viscosity of air (Pa.s)
U_infinity = 40; free stream velocity (m/s)
Re_L = rho * U_infinity * L / mu; % Reynolds number based on length L"""

# Define columns for the layout
cols = st.columns(2)
col1, col2, col3 = st.columns(3)

with cols[0]:
    matlab_code = st.text_area('MATLAB Code', value=sample_matlab_code, height=300, help="Paste your MATLAB code here.")
    # matlab_code = st.code('MATLAB Code', value=sample_matlab_code, height=300, help="Paste your MATLAB code here.")

with cols[1]:
    # Initialize session_state variable if it does not exist
    if 'python_code' not in st.session_state:
        st.session_state.python_code = "# Translated Python code will appear here"

    # Placeholder for the Python code text area
    # python_code = st.text_area("Python Code", value=st.session_state.python_code, height=300, help="The translated Python code will appear here.")

    python_code_placeholder = st.empty()

# The actual translation logic from the old version
if st.button('Translate MATLAB to Python'):
    try:
        # API call to refactor the code
        message = [{"role": "user", "content": gpt_prompt + matlab_code}]
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=message,
            temperature=0.9,
            max_tokens=1000,
            frequency_penalty=0.0
        )
        
        # Extract the code from the response
        translated_code = response.choices[0].message['content']

        # Update the session_state variable
        st.session_state.python_code = translated_code
        # Display the updated Python code in the placeholder
        python_code_placeholder.text_area("Python Code", value=st.session_state.python_code, height=300, help="The translated Python code will appear here.")

    except Exception as e:
        st.error(f"Error in translation: {e}")

# About section in sidebar, keep it as in the latest version
with st.sidebar:
    st.header('About')
    st.info('This app uses GPT-4 to refactor MATLAB code to Python. It is designed for educational purposes in the field of aerospace engineering.')
    st.sidebar.slider("Temperature (placeholder)")