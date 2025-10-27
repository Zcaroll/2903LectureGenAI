from google import genai # Importing the genai library from the google
import rich
from rich.markdown import Markdown

client = genai.Client() # client object in charge of connecting to googles servers
chat = client.chats.create(model='gemini-2.5-flash')

while True:
    # ask user for input, send message to chat model
    prompt = input("Enter your message: ")
    response = chat.send_message(prompt + 'Answer in a short sentence.')
    #print(response.text)
    rich.print(Markdown(response.text)) # nicely formatted markdown output
    print(response.usage_metadata.total_token_count) # token count