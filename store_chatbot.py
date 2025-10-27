from google import genai
from google.genai.types import GenerateContentConfig
import rich # library for rich text and beautiful formatting in the terminal
from rich.markdown import Markdown

client = genai.Client()
chat =client.chats.create(model='gemini-2.5-flash')


while True:
    # ask user for input, set up parameters for chat model
    question = input("Ask your question for our store: ")
    response = chat.send_message(
        #model='gemini-2.5-flash',
        question,
        config=GenerateContentConfig(
            # hypothetical chattbot for vans. system instructions set accordingly
            system_instruction="""You are Jane, the chatbot representing Vans.
            You help customers find shoes, provide fashion advice, and answer questions about store policies.
            You are a young, active, on trend chatbot. Be friendly and engaging in your responses."""
        )
    )


    rich.print(Markdown(response.text))