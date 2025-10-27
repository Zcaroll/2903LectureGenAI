from google import genai # Importing the genai library from the google
import rich
from rich.markdown import Markdown

client = genai.Client() # client object in charge of connecting to googles servers

response = client.models.generate_content( # cotains the response from the model as well as metadata
    model='gemini-2.5-flash',  # Specifying the model
    contents='Why are firetrucks red? Explain simply.'  # The prompt for content generation

)

#print(response.text)
rich.print(Markdown(response.text)) # nicely formatted markdown output
print(response.usage_metadata) # token count and other metadata