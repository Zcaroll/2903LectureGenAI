from google import genai # Importing the genai library from the google

client = genai.Client() # client object in charge of connecting to googles servers

response = client.models.generate_content( # cotains the response from the model as well as metadata
    model='gemini-2.5-flash',  # Specifying the model
    contents="""We run a paperclip business in new york,  
    we are not reaching our sales goals for the quarter. 
    What are some strategies we can use to increase our sales?' """
)

print(response.text)