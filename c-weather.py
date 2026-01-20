#this code runs without caching technique

import requests
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load variables from .env
load_dotenv()

# Get the API key
api_key = os.getenv("OPENAI_API_KEY")

# Your API key
client = OpenAI(api_key=api_key)

def get_weather(city):
    api_key = os.getenv("WEATHER_API_KEY")
    url= f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"
    data = requests.get(url).json()
    condition = data["current"]["condition"]["text"]
    temp_c = data["current"]["temp_c"]
    return f"{condition}, {temp_c}°C"




# Ask the AI, and provide the live data
city_name = input("Enter a city: ")
city = city_name
weather = get_weather(city)
prompt = f"The current weather in {city_name} is exactly {weather}. Explain deep chemistry behind it + why. Give structured and Joker-like response"

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}]
)

print(response.choices[0].message.content)


  # User types city dynamically
weather = get_weather(city_name)
 