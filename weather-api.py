
"""
This code fetches the current weather data for Fargo using the OpenWeatherMap API. It prints the city name, temperature in Fahrenheit, weather description, and humidity. You can replace "Fargo" with any other city to get its weather data. Make sure to replace "YOUR_API_KEY" with your actual API key from OpenWeatherMap.
"""

import requests
import os
from dotenv import load_dotenv # type: ignore

# Load environment variables from .env file
load_dotenv()

 
API_KEY = os.getenv("OPEN_WEATHER_API_KEY")
CITY = "Fargo"
url = "https://api.openweathermap.org/data/2.5/weather"


params = {
    "q": CITY,
    "appid": API_KEY,
    "units": "imperial"   # use "imperial" for Fahrenheit
}

try:
    response = requests.get(url, params=params)
    data = response.json()

    print("City:", data["name"])
    print("Temperature:", data["main"]["temp"])
    print("Weather:", data["weather"][0]["description"])
    print("Humidity:", data["main"]["humidity"])  
except Exception as e:
    print(f"Error fetching weather data: {e}")    





# import requests
# import pandas as pd
# import random
# from datetime import datetime, timedelta
# import time

# API_KEY = "YOUR_API_KEY"
# regions = {
#     "North": (40.7128, -74.0060),
#     "South": (29.7604, -95.3698),
#     "East": (42.3601, -71.0589),
#     "West": (34.0522, -118.2437),
#     "Central": (41.8781, -87.6298)
# }

# records = []
# num_rows = 500
# start_date = datetime(2024, 1, 1)
# end_date = datetime(2025, 12, 31)
# total_seconds = int((end_date - start_date).total_seconds())

# for i in range(num_rows):
#     region = random.choice(list(regions.keys()))
#     lat, lon = regions[region]

#     timestamp = start_date + timedelta(seconds=random.randint(0, total_seconds))
#     unix_time = int(timestamp.timestamp())

#     url = f"https://api.openweathermap.org/data/2.5/onecall/timemachine?lat={lat}&lon={lon}&dt={unix_time}&appid={API_KEY}&units=metric"
#     response = requests.get(url)
#     data = response.json()

#     # pick first hourly reading
#     if "hourly" in data and len(data["hourly"]) > 0:
#         weather = data["hourly"][0]
#         temp = weather.get("temp")
#         humidity = weather.get("humidity")
#         wind_speed = weather.get("wind_speed")
#         precipitation = weather.get("rain", {}).get("1h", 0)  # rain in last hour
#         weather_event = weather.get("weather", [{}])[0].get("main", "")

#         records.append({
#             "weather_id": f"WEA{i:05d}",
#             "region": region,
#             "timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S"),
#             "temperature": temp,
#             "humidity": humidity,
#             "precipitation": precipitation,
#             "wind_speed": wind_speed,
#             "weather_event": weather_event
#         })
    
#     time.sleep(1)  # avoid hitting API rate limits

# df = pd.DataFrame(records)
# df.to_csv("weather_data_500.csv", index=False)