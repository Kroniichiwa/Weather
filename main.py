from flask import Flask
from flask_restful import Api,Resource

app = Flask(__name__)
api = Api(app)

weather_data = [
    {
        "location": "New York",
        "temperature": 12.3,
        "humidity": 60,
        "wind_speed": 6.7,
        "wind_direction": "NW",
        "description": "Cloudy"
    },
    {
        "location": "Los Angeles",
        "temperature": 22.8,
        "humidity": 45,
        "wind_speed": 3.2,
        "wind_direction": "SE",
        "description": "Sunny"
    },
    {
        "location": "London",
        "temperature": 8.9,
        "humidity": 75,
        "wind_speed": 9.4,
        "wind_direction": "SW",
        "description": "Rainy"
    },
    {
        "location": "Paris",
        "temperature": 13.5,
        "humidity": 55,
        "wind_speed": 5.6,
        "wind_direction": "NE",
        "description": "Partly cloudy"
    },
    {
        "location": "Tokyo",
        "temperature": 18.2,
        "humidity": 50,
        "wind_speed": 2.8,
        "wind_direction": "E",
        "description": "Clear"
    },
    {
        "location": "Sydney",
        "temperature": 26.7,
        "humidity": 35,
        "wind_speed": 10.2,
        "wind_direction": "W",
        "description": "Mostly sunny"
    },
    {
        "location": "Moscow",
        "temperature": -2.8,
        "humidity": 85,
        "wind_speed": 12.3,
        "wind_direction": "N",
        "description": "Snowy"
    },
    {
        "location": "Rio de Janeiro",
        "temperature": 29.5,
        "humidity": 70,
        "wind_speed": 4.5,
        "wind_direction": "SE",
        "description": "Partly cloudy"
    },
    {
        "location": "Cape Town",
        "temperature": 19.8,
        "humidity": 65,
        "wind_speed": 6.2,
        "wind_direction": "SW",
        "description": "Sunny"
    },
    {
        "location": "Toronto",
        "temperature": -5.6,
        "humidity": 50,
        "wind_speed": 8.9,
        "wind_direction": "NW",
        "description": "Snowy"
    }
]

class Weather(Resource):
    def get(self) :
        result = weather_data
        return result

#call
api.add_resource(Weather,"/Weather")

if __name__ == "__main__" :
    # Not recommend using in a big environment
    app.run(debug=True)
