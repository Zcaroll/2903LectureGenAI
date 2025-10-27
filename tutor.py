from google import genai
from google.genai.types import GenerateContentConfig
import rich # library for rich text and beautiful formatting in the terminal
from rich.markdown import Markdown

client = genai.Client()
chat =client.chats.create(model='gemini-2.5-flash')


while True:
    question = input("Ask your question to the Java programming tutor: ")
    response = chat.send_message(
        #model='gemini-2.5-flash',
        question,
        config=GenerateContentConfig(
            system_instruction="""You are a helpful programming tutor for Java programming students
            You can explain concepts and programs but don't give the user the answers directly.
            If the user asks for code, ask them questions and help them write it themselves.
            Be patient and encouraging at all times.""",
        )
    )


    rich.print(Markdown(response.text))