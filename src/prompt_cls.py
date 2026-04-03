# prompt_cls.py
## You will need to replace all #PLACEHOLDER# lines  
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

# Define a prompt template with placeholders
template = """
You are a helpful assistant.
Summarize the following text in one sentence:
{text}
"""

# Create the PromptTemplate object
prompt = PromptTemplate(
    input_variables=["text"],  # placeholders in the template
    template=template
)
# Initialize the Gemini LLM
#PLACEHOLDER#

#Function to get user input and generate response
def chat_to_llm():
    while True:
       # collect user_input or quit to quit (check lower case )
        #PLACEHOLDER#
        #PLACEHOLDER#
            break
        # Format the prompt with user input
        #PLACEHOLDER#
        # Get response from LLM
       #PLACEHOLDER#
        print("Summary:", response.content)        

if __name__ =="__main__":
    chat_to_llm()

# Previous Example COde
#filled_prompt = prompt.format(text="Utilizing chatbots and AI agents that react in real time to deliver more accurate and personalized responses using your own datasets. \
#Synthesizing data to understand customer profiles and generating content to reach target customers.")
#print(filled_prompt)
