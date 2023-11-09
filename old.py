from dotenv import load_dotenv
import openai
import os
import streamlit as st

# Load the API key from the .env file
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

# Define the gpt_prompt outside of any Streamlit interaction to avoid it being reset
gpt_prompt = """
you will act as a matlab to python refactoring machine. I will paste matlab code and you will just output the refactored code in python, including not too verbose but useful comments. Important: do not output anything beside the code — this is powering a refactoring app within an aerospace university research program via gpt-4 API. REQUIREMENTS: python 3.9, numpy, matplotlib, scipy, simpy, pandas. The code to refactor is:
"""

# Title and introduction from the latest version
st.title('MATLAB to Python Refactorer')
st.write('Effortlessly refactor your MATLAB code to Python with the power of GPT-4.')

# Sample MATLAB code for demonstration purposes, keep it as in the old version
sample_matlab_code = """
% Sample MATLAB code for CFD
rho = 1.225; % density of air (kg/m^3)
mu = 1.7894e-5; % dynamic viscosity of air (Pa.s)
U_infinity = 40; % free stream velocity (m/s)
Re_L = rho * U_infinity * L / mu; % Reynolds number based on length L
"""

# Define columns for the layout as in the latest version
cols = st.columns(2)

with cols[0]:
    matlab_code = st.text_area('MATLAB Code', value=sample_matlab_code, height=300, help="Paste your MATLAB code here.")

with cols[1]:
    # Placeholder for Python code, use the same logic as MATLAB code area
    python_code = st.text_area("Python Code", value="", height=300, help="The translated Python code will appear here.", key="python_code")

# The actual translation logic from the old version
if st.button('Translate MATLAB to Python'):
    try:
        # API call to refactor the code
        message = [{"role": "user", "content": gpt_prompt + matlab_code}]
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=message,
            temperature=0.2,
            max_tokens=1000,
            frequency_penalty=0.0
        )
        # Extract the code from the response
        python_code = response.choices[0].message['content']

        # Update the Python code area with the translated code
        st.session_state.python_code = python_code
    except Exception as e:
        st.error(f"Error in translation: {e}")

# About section in sidebar, keep it as in the latest version
with st.sidebar:
    st.header('About')
    st.info('This app uses GPT-4 to translate MATLAB code to Python. It is designed for educational purposes in the field of aerospace engineering.')
