from dotenv import load_dotenv
import openai
import os

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

gpt_prompt = """
you will act as a matlab to python refactoring machine. I will paste matlab code and you will just output the refactored code in python, including not too verbose but useful comments. Important: do not output anything beside the code — this is powering a refactoring app within an aerospace university research program via gpt-4 API. REQUIREMENTS: python 3.9, numpy, matplotlib, scipy, simpy, pandas. The code to refactor is:
"""
print(gpt_prompt)

matlab_code = input("Sample matlab code test1 hello from seank the prod pirate")

message=[{"role": "user", "content": gpt_prompt + matlab_code}]
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages = message,
    temperature=0.2,
    max_tokens=1000,
    frequency_penalty=0.0
)
print(response)