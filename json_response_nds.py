# nds for 'no defined structure'
from google import genai # Importing the genai library from the google
from google.genai.types import GenerateContentConfig
from pydantic import BaseModel

# creating a schema for the json response
class RecipeResponse(BaseModel):
    recipe_name: str
    ingredients: list[str]
    instructions: list[str]




client = genai.Client() # client object in charge of connecting to googles servers

response = client.models.generate_content( # cotains the response from the model as well as metadata
    model='gemini-2.5-flash',  # Specifying the model
    contents='I have leftover chicken, cheese, and brocolli. Suggest a recipe?'  # The prompt for content generation
    config=GenerateContentConfig(
        response_mime_type='application/json'  # specifying that we want the response in json format
        response_schema=Recipe # specifying the schema created earlier for the response
    )


)

print(response.text) 
recipe = response.parsed # a recipe object
print(recipe.recipe_name)

for ingredient in recipe.ingredients:
    print(f"- {ingredient}")

for step in recipe.instructions:
    print(step)
