import streamlit as st
from openai import OpenAI

# Load OpenAI API key
openai_client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Define gpt-4 outside of Streamlit instance
gpt_prompt = """you will act as a matlab to python and vice-versa refactoring machine. I will show you either matlab or python code and you will just output the refactored code in the other language, including not too verbose but useful comments. Important: do not output anything beside the refactored code, not even the ```python or ```matlab code block formatting. Your response is powering an aerospace refactoring app so I need only the raw output. Requirements.txt: python 3.9, numpy, matplotlib, scipy, simpy, pandas. The code to refactor is: 
"""

# UI elements
st.title('matlab 🔄 python refactor')
st.write('Paste MATLAB or Python code and get Python equivalent refactored by GPT-4.')

# Sample MATLAB code for demonstration purposes
sample_matlab_code = """% MATLAB code for plotting a function and its gradient
[x, y] = meshgrid(-2:0.1:2, -2:0.1:2); % Create a 2D grid of x and y values
f = x.^2 - y.^2;                       % Define the function f(x, y)

% Calculate the gradient of f
[fx, fy] = gradient(f, 0.1, 0.1);

% Plot the function
surf(x, y, f);
title('Function f(x, y) = x^2 - y^2 and its Gradient');
hold on;

% Plot the gradient vectors
quiver(x, y, fx, fy, 'r');
hold off;"""


matlab_code = st.text_area('MATLAB Code', value=sample_matlab_code, height=300, help="Paste your MATLAB code here.")

# Placeholders for MATLAB and Python code blocks
matlab_code_block_placeholder = st.empty()
python_code_block_placeholder = st.empty()

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

        # Display MATLAB and Python code side by side
        col1, col2 = st.columns(2)
        
        with col1:
            st.code(matlab_code, language='matlab')
        with col2:
            st.code(translated_code, language='python')

    except Exception as e:
        st.error(f"Error in translation: {e}")

# About section in sidebar
with st.sidebar:
    st.header('About')
    st.info('This app uses GPT-4 to refactor MATLAB code to Python. It is designed for educational purposes in the field of aerospace engineering.')
    # The slider is a placeholder and does not affect the temperature setting in the API call above
    st.sidebar.slider("Response length")
