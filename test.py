import requests
import json

#port
BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "/Weather", {})
weather_dict = json.loads(response.content)

country = input("Please input the country name : ")

for item in weather_dict:
    if country == item['location'] :
        print(f"Location: {item['location']}")
        print(f"Temperature: {item['temperature']} °C")
        print(f"Description: {item['description']}")


