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

# Title and introduction
st.title('CFD Translator 0.1')
st.write('Refactor MATLAB to Python for Computational Fluid Dynamics with ease.')

# Sample MATLAB code for demonstration purposes
sample_matlab_code = """
% Sample MATLAB code for CFD
rho = 1.225; % density of air (kg/m^3)
mu = 1.7894e-5; % dynamic viscosity of air (Pa.s)
U_infinity = 40; % free stream velocity (m/s)
Re_L = rho * U_infinity * L / mu; % Reynolds number based on length L
"""

# Input text area for MATLAB code
matlab_code = st.text_area('MATLAB Code', value=sample_matlab_code, height=300, help="Paste your MATLAB code here or use the sample to test the translation.")

# The actual translation button
if st.button('MATLAB to Python'):
    try:
        # Prepare the message payload
        message = [{"role": "user", "content": gpt_prompt + matlab_code}]
        
        # Call the OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=message,
            temperature=0.2,
            max_tokens=1000,
            frequency_penalty=0.0
        )

        # Extract the code from the response
        python_code = response.choices[0].message['content']
        
        # Display the translated Python code
        st.text_area("Python Code", python_code, height=300, help="The translated Python code will appear here.")

    except Exception as e:
        st.error(f"Error in translation: {e}")

# Side notes about the application
st.sidebar.header('About')
st.sidebar.info('Yay! CFD Translator 0.1 is your AI-powered sidekick to seamlessly convert MATLAB code into Python, specifically for Computational Fluid Dynamics. Happy translating!')
