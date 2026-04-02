# prompt_cls.py
from langchain_core.prompts import PromptTemplate

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

# Example 
filled_prompt = prompt.format(text="Utilizing chatbots and AI agents that react in real time to deliver more accurate and personalized responses using your own datasets. \
Synthesizing data to understand customer profiles and generating content to reach target customers.")
print(filled_prompt)
