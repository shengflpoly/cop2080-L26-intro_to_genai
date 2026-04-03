# summarize_text_cls.py
import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
 
load_dotenv()

def main():
    print("Hello from COP2080!")
   #PLACEHOLDER#
  
    summary_prompt_template = PromptTemplate(
        input_variables=["#PLACEHOLDER#"], template=summary_template
    )

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",  temperature=0
    )
    chain = summary_prompt_template | #PLACEHOLDER#

    response = chain.invoke(input={"#PLACEHOLDER#": info})
    print(response.content)

if __name__ == "__main__":
    main()
