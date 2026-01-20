##this code runs with caching technique (calling once weather API if applicable to reduce API cost) 

import requests
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load variables from .env
load_dotenv()

# OpenAI key
openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)

# Weather API key
weather_api_key = os.getenv("WEATHER_API_KEY")

# Simple in-memory cache
weather_cache = {}  # dictionary to store city -> weather info

def get_weather(city):
    # Check if city is already in cache
    if city in weather_cache:
        print(f"Using cached weather for {city}")
        return weather_cache[city]
    
    # If not cached, call the API
    url = f"http://api.weatherapi.com/v1/current.json?key={weather_api_key}&q={city}&aqi=no"
    data = requests.get(url).json()
    condition = data["current"]["condition"]["text"]
    temp_c = data["current"]["temp_c"]


    if temp_c > 5:
        word = "Nice"
    elif temp_c < 5 and temp_c > 0:
        word = "Good good"
    else:
        word = "A bit chilly"

    
    weather_info = f"{condition}, {temp_c}°C. {word} in {city}!"
    
    # Save to cache
    weather_cache[city] = weather_info
    
    return weather_info

# Main loop: ask AI about cities
while True:
    city_name = (input("Enter a city (or 'q' to exit): ")).capitalize() 
    if city_name.lower() == "q":
        break

    # Get weather (cached if already asked)
    weather = get_weather(city_name)
    
    # AI prompt
    prompt = f"The current weather in {city_name} is exactly {weather}. Explain deep physics/georaphy behind it + why. Give structured response."
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    
    print(response.choices[0].message.content)
    #print(f"Weather in {city_name}: {weather}\n")
