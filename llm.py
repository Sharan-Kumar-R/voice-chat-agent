from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

def batch(user_input):
    chat = ChatGroq(temperature=0, model_name="llama3-70b-8192", groq_api_key=os.getenv("GROQ_API_KEY"))

    system = "You are a helpful assistant."
    prompt = ChatPromptTemplate.from_messages([("system", system), ("human", "{text}")])

    chain = prompt | chat
    response = chain.invoke({"text": user_input})
    print("\nResponse:\n", response.content)

def streaming(user_input):
    chat = ChatGroq(temperature=0, model_name="llama3-70b-8192", groq_api_key=os.getenv("GROQ_API_KEY"))
    prompt = ChatPromptTemplate.from_messages([("system", "You are a helpful assistant."), ("human", "{text}")])
    chain = prompt | chat
    print("\nStreaming response:\n")
    for chunk in chain.stream({"text": user_input}):
        print(chunk.content, end="", flush=True)

if __name__ == "__main__":
    mode = input("Choose mode (batch/streaming): ").strip().lower()
    user_input = input("Enter your prompt: ")
    if mode == "batch":
        batch(user_input)
    elif mode == "streaming":
        streaming(user_input)
    else:
        print("Invalid mode. Please enter 'batch' or 'streaming'.")
