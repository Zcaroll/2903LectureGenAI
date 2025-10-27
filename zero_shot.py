from google import genai # Importing the genai library from the google

client = genai.Client() # client object in charge of connecting to googles servers

response = client.models.generate_content( # cotains the response from the model as well as metadata
    model='gemini-2.5-flash',  # Specifying the model
    # workout related prompt instead of business. cusious how the model responds
    contents="""I am trying to increase the strenth and size of my arms,
    what are some effective exercises and routines I can follow?"""
    # The prompt does not include any prior examples
)

print(response.text)