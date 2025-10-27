from google import genai
from google.genai.types import GenerateContentConfig
import rich # library for rich text and beautiful formatting in the terminal
from rich.markdown import Markdown
import sys

client = genai.Client()
chat =client.chats.create(model='gemini-2.5-flash')

# safety check for system instruction file
try:
    with open('chat_system_instruction.txt', 'r') as f:
        system_instruction_text = f.read()
except:
    print('Missing system instuction. Quiting...')
    sys.exit()

while True:
    # ask user for input, set up parameters for chat model
    question = input("Ask your question for our store: ")
    response = chat.send_message(
        #model='gemini-2.5-flash',
        question,
        config=GenerateContentConfig(
            # hypothetical chattbot for vans. system instructions set accordingly
            system_instruction=system_instruction_text
        )
    )


    rich.print(Markdown(response.text))