from google import genai # Importing the genai library from the google

client = genai.Client() # client object in charge of connecting to googles servers

response = client.models.generate_content( # cotains the response from the model as well as metadata
    model='gemini-2.5-flash',  # Specifying the model
    contents="""I am trying to increase the strenth and size of my arms,
    what are some effective exercises and routines I can follow?
    Last year I tried bicep curls with 20lb weights and did not see much progress.
    The year before that, I focused on push-ups and saw some improvement.
    Three years ago, I did pull-ups but struggled to do more than five at a time."""
    # The prompt includes prior examples
)

print(response.text)