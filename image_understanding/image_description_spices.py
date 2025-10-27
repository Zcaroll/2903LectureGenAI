from google import genai
from google.genai import types
from pydantic import BaseModel

client = genai.Client() # client object in charge of connecting to googles servers

# creating a schema for the json response
class Spices(BaseModel):
    spice_names: str
    colors: str



# Read image file and stores as bytes
with open('spice_cabinet.jpg', 'rb') as f: # picture i took
    image_bytes = f.read()


response = client.models.generate_content(
    model='gemini-2.5-flash',  # Specifying the model
    contents=[
        types.Part.form_bytes(data=image_bytes, mime_type='image/jpeg'), # image format to properly reconstuct the image
        'What spices are in this picture?'
    ],
    config=types.GenerateContentConfig(
        system_instruction="Identify the spices in the image and provide their common names and colors.",
        response_mime_type='text/plain'
        response_schema=list[Spices] # specifying the schema created earlier for the response
    )
)

print(response.parsed) # a list of Spices objects

for spice in response.parsed:
    print(f"Spice Names: {spice.spice_names}")
    print(f"Colors: {spice.colors}")