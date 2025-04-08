from langchain_core.prompts import ChatPromptTemplate

sentiment_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an AI that analyzes customer feedback and provides a sentiment classification (Positive, Negative, Neutral) and a helpful recommendation."),
    ("user", "Text: {text}")
])
