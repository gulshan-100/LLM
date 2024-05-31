import langchain
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.output_parsers import CommaSeparatedListOutputParser
from langchain.output_parsers import NumberedListOutputParser
from langchain.output_parsers import JsonOutputKeyToolsParser

import os
os.environ['GOOGLE_API_KEY'] = "api_key"

output_parser = JsonOutputKeyToolsParser()
format_instructions = output_parser.get_format_instructions()
print(format_instructions)

prompt = PromptTemplate(
    template="Provide 5 examples of {query}.\n{format_instructions}",
    input_variables=["query"],
    partial_variables={"format_instructions": format_instructions}
)

llm = ChatGoogleGenerativeAI(model='gemini-pro')

formatted_prompt = prompt.format(query='currencies')

response = llm.invoke(formatted_prompt)

print(response.content)
