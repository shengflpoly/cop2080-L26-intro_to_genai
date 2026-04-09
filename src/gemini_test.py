# gemini test
from dotenv import load_dotenv
from google import genai

load_dotenv()
# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()
use_model = "gemini-2.5-flash"
response = client.models.generate_content(
    model=use_model, contents="Who is the father of AI?"
)
print(response.text)
