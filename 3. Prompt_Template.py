from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts.prompt import PromptTemplate


import os 
os.environ["GOOGLE_API_KEY"] = "AIzaSyCBpGHIaubNnku2U3I2Fm3PCkQ3ldfHxRA"  # Replace with your actual API key

llm = ChatGoogleGenerativeAI(model='gemini-pro')

topic = input("Topic:")
words = int(input("Words count:"))

template = """
Explain {topic} in {words} words
"""
prompt = PromptTemplate(
    input_variables=['topic', 'words'],
    template=template
)

final_prompt = prompt.format(topic = topic, words = words)

result = llm.invoke(final_prompt)
print(result.content)

