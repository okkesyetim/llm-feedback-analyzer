from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from prompts import sentiment_prompt

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.3,
    google_api_key=os.getenv("GEMINI_API_KEY"),
    convert_system_message_to_human=True
)

parser = StrOutputParser()

sentiment_chain = sentiment_prompt | model | parser
