from google import genai
from google.genai import types

client = genai.Client() # client object in charge of connecting to googles servers

# Read image file and stores as bytes
with open('frog_statue.jpg', 'rb') as f: # picture i took
    image_bytes = f.read()


response = client.models.generate_content(
    model='gemini-2.5-flash',  # Specifying the model
    contents=[
        types.Part.form_bytes(data=image_bytes, mime_type='image/jpeg'), # image format to properly reconstuct the image
        'What is this a picture of?'
    ]
)

print(response.text)
