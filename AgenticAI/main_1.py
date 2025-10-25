# import getpass
import os
from dotenv import load_dotenv

# if not os.environ.get("GROQ_API_KEY"):
#   os.environ["GROQ_API_KEY"] = getpass.getpass("Enter API key for Groq: ")

from langchain.chat_models import init_chat_model


load_dotenv()

model = init_chat_model("llama-3.1-8b-instant", model_provider = "groq")

response = model.invoke("who is virat kohli")
print(response.content)