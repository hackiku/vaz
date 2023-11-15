import streamlit as st
from openai import OpenAI

# Load OpenAI API key
openai_client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Function to call OpenAI API
def call_openai_api(prompt):
    try:
        chat_completion = openai_client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="gpt-4",
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        st.error(f"Error in OpenAI API call: {e}")
        return None

# Define prompts
refactor_prompt = """you will act as a matlab to python and vice-versa refactoring machine. I will show you either matlab or python code and you will just output the refactored code in the other language, including not too verbose but useful comments. Important: do not output anything beside the refactored code, as your response is powering an aerospace refactoring app so I need only the raw output. Of course keep in mind best practices and tools for each language and make the refactor functional (e.g. when doing python -> matlab, no need to import package, etc). The code to refactor is: 
"""
# Requirements.txt: python 3.9, numpy, matplotlib, scipy, simpy, pandas


# UI elements
st.title('MATLAB 🔄 Python Refactor')
st.write('Paste MATLAB or Python code and get its equivalent in the other language refactored by GPT-4.')

# Sample MATLAB code used as placeholder
placeholder_code = """[x, y] = meshgrid(-2:0.1:2, -2:0.1:2); % Create a 2D grid of x and y values
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

# user inputs
user_code = st.text_area('Code to refactor', placeholder=placeholder_code, height=300, help="Paste your MATLAB or Python code here.")
word_count = st.slider("Word count for AI explanation", min_value=50, max_value=300, value=150, step=1)

# refactor logic
if st.button('🔄 Translate Code'):
    if not user_code: # if no user input, refactor placeholder code as demonstration
        user_code = placeholder_code
    refactored_code = call_openai_api(refactor_prompt + user_code)
    if refactored_code:
        col1, col2 = st.columns(2)
        with col1:
            st.code(user_code, language='matlab')
        with col2:
            st.code(refactored_code, language='python')

# interpretation logic
if st.button('🧑‍🏫 Interpret Code'):
    interpret_prompt = f"""you will interpret the following MATLAB or python code from an aerospace engineering perspective, explaining its purpose and functionality in simple terms. Reprint code samples and formulas in markdown-compatible format whenever possible. Make your response {word_count} words long. The code to interpret is:
    """
    interpretation = call_openai_api(interpret_prompt.replace("$word_count", str(word_count)) + user_code)
    if interpretation:
        st.markdown("### Interpretation")
        st.write(interpretation)
        
# About section in sidebar
with st.sidebar:
    st.header('About')
    st.info('REFACTORRR This app uses GPT-4 to refactor and interpret code. It is designed for educational purposes in the field of aerospace engineering.')

# TODO add Google Drive link for user file uploads


