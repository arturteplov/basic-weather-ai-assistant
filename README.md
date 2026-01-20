# Weather + OpenAI Assistant

This project is a Python-based AI assistant that fetches **real-time weather data** for any city using [WeatherAPI.com](https://www.weatherapi.com/) and generates structured explanations using **OpenAI GPT-3.5**. It supports both:

1. **`c-weather.py`** – basic version without caching (calls WeatherAPI every time).  
2. **`p-weather.py`** – optimized version with caching (reduces API calls by storing city weather locally during runtime).

---

 
## **Features**

- Fetch live weather for any city.
- AI-generated explanations about weather using OpenAI.
- Caching to reduce API costs and speed up repeated requests.
- Dynamic city input from the user.
- Optional “fun” descriptions based on temperature.

---

## **Setup**

### **1. Clone the repository**

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/basic-weather-ai.git
cd basic-weather-ai
```
### **2. Create a virtual environment (recommended)
```bash
python3 -m venv venv
source venv/bin/activate      # macOS / Linux
venv\Scripts\activate         # Windows
```
### **3. Install dependencies**
```bash
pip install -r requirements.txt
```
requirements.txt should contain:
```bash
requests
python-dotenv
openai
```
### **4. Create a .env file**
OPENAI_API_KEY=sk-YOUR_OPENAI_KEY
WEATHER_API_KEY=YOUR_WEATHERAPI_KEY

---

## **Usage**

### **1. Run basic weather assistant (no caching + chemistry explanation)
```bash
python c-weather.py
```
- Enter any city name when prompted.
- The AI will fetch the live weather and give a chemistry-based explanation.

### **2. Run cached weather assistant (+ physics/georgraphy explanation)
```bash
python p-weather.py
```
- Enter city names in the loop.
- If the same city is entered again, the program uses cached data to save API calls.
- Type q to exit the loop.