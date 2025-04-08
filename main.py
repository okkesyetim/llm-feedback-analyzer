from fastapi import FastAPI
from langserve import add_routes
from chains import sentiment_chain
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="SentimentSage - Gemini API",
    version="1.0",
    description="Analyze text sentiment and generate helpful recommendations using Gemini + LangChain"
)

add_routes(
    app,
    sentiment_chain,
    path="/analyze"
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
