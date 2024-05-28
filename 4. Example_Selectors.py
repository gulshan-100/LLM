import langchain 
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain import FewShotPromptTemplate
from langchain import PromptTemplate, FewShotPromptTemplate

#from langchain_core.prompts.few_shot import FewShotPromptTemplate
import os 
os.environ['GOOGLE_API_KEY'] = "api_key"

llm = ChatGoogleGenerativeAI(model = 'gemini-pro')

#Prompt template generattion 
our_prompt = """You are a comedian who roasts everyone's question:

Question: How to become comedian?
Response: """

#Redefine the prompts 
new_prompt = """You are a comedian who raosts everyone asking questions to him:
Here are some examples:

Question: How to become comedian?
Response: You can become comedian when you have nothing to do in life, no careers option with your education.

Question: What are life dreams?
Response: It is the vision, which you cannot accomplish.

Question: How you define a engineering student?
Response: 
"""

result = llm.invoke(new_prompt)

#Few shot prompt template 
examples = [
    {
    "query":"How to study?",
    "answer":"Nothing just take blanket on body, take book in hand and study in sleeping"
    },
    {
    "query":"How to read books?",
    "answer":"Start from the top and read till the end with eyes closed."
    }
]

example_template = """
Question: {query}
Response: {answer}
"""


example_prompt = PromptTemplate(
    input_variables = ["query","answer"],
    template = example_template
)

prefix = """Suppose you are a engineering student  who is filled with engineering in this mind:
Here are some examples:
"""

suffix = """
Question: {userInput}
Response: """

few_shot_prompt_template = FewShotPromptTemplate(
    examples = examples,
    example_prompt = example_prompt,
    prefix =prefix,
    suffix = suffix,
    input_variables = ["userInput"],
    #example_seperator = "\n\n"
)

query = "What is the laptop?"

print(few_shot_prompt_template.format(userInput = query))

print(llm.invoke(few_shot_prompt_template.format(userInput=query)).content)