import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

st.header('QnA LLM Application')

import os
os.environ["GOOGLE_API_KEY"] = "api_key"

def get_text():
    input_text = st.text_input("You: ", key="input")
    return input_text

def load_answer(question):
    llm = ChatGoogleGenerativeAI(model="gemini-pro",temperature=0)
    answer=llm.invoke(question)
    return answer

user_input=get_text()
response = load_answer(user_input)
submit = st.button('Generate')  

#If generate button is clicked
if submit:
    st.subheader("Answer:")
    st.write(response.content)