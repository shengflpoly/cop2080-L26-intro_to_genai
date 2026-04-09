# summarize_text_cls.py
import os

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

def main():
    print("Hello from COP2080!")
    movie = """
    On the lush alien world of Pandora live the Na'vi, beings who appear primitive but are highly evolved. Because the planet's environment is poisonous, human/Na'vi hybrids, called Avatars, must link to human minds to allow for free movement on Pandora. Jake Sully (Sam Worthington), a paralyzed former Marine, becomes mobile again through one such Avatar and falls in love with a Na'vi woman (Zoe Saldana). As a bond with her grows, he is drawn into a battle for the survival of her world.
    """
    summary_template = """
    You are a helpful assistant.
    create a “1. A brief summary”, “2. An exciting element of the movie”, and “3. The main actors” of the input text.
    {movie}
    """
  
    summary_prompt_template = PromptTemplate(
        input_variables=["movie"], template=summary_template
    )

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",  temperature=0
    )
    chain = summary_prompt_template | llm

    response = chain.invoke(input={"movie": movie})
    print(response.content)

if __name__ == "__main__":
    main()
