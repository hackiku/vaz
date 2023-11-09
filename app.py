import streamlit as st
from openai import OpenAI

# Load OpenAI API key
openai_client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

gpt_prompt = """you will act as a matlab to python refactoring machine. I will paste matlab code and you will just output the refactored code in python, including not too verbose but useful comments. Important: do not output anything beside the code, not even the ```python code block formatting. Your response is powering an aerospace refactoring app so I need only the raw output. REQUIREMENTS: python 3.9, numpy, matplotlib, scipy, simpy, pandas. The code to refactor is: 
# Define gpt-4 outside of Streamlit instance
"""

# UI elements
st.title('MATLAB to Python Refactorer')
st.write('Paste MATLAB code and get Python equivalent refactored by GPT-4.')

# Sample MATLAB code for demonstration purposes
sample_matlab_code = """% Sample MATLAB code for CFD
rho = 1.225; % density of air (kg/m^3)
mu = 1.7894e-5; % dynamic viscosity of air (Pa.s)
U_infinity = 40; % free stream velocity (m/s)
Re_L = rho * U_infinity * L / mu; % Reynolds number based on length L"""

# Define columns for the layout
cols = st.columns(2)

with cols[0]:
    matlab_code = st.text_area('MATLAB Code', value=sample_matlab_code, height=300, help="Paste your MATLAB code here.")

with cols[1]:
    python_code_placeholder = st.empty()

# The actual translation logic
if st.button('Translate MATLAB to Python'):
    try:
        # API call to refactor the code
        chat_completion = openai_client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": gpt_prompt + matlab_code
                }
            ],
            model="gpt-4",
        )
        
        # Extract the code from the response
        translated_code = chat_completion.choices[0].message.content

        # Update the Python code in the placeholder
        python_code_placeholder.text_area("Python Code", value=translated_code, height=300, help="The translated Python code will appear here.")

    except Exception as e:
        st.error(f"Error in translation: {e}")

# About section in sidebar
with st.sidebar:
    st.header('About')
    st.info('This app uses GPT-4 to refactor MATLAB code to Python. It is designed for educational purposes in the field of aerospace engineering.')
    # The slider is a placeholder and does not affect the temperature setting in the API call above
    st.sidebar.slider("Temperature (placeholder)")
