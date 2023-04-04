from flask import Blueprint, request, jsonify
from weather.controller import WeatherController

weather_bp = Blueprint('weather', __name__)

@weather_bp.route('/weather', methods=['POST'])
def create_weather():
    city = request.json['city']
    temperature = request.json['temperature']
    description = request.json['description']
    weather = WeatherController.create_weather(city, temperature, description)
    return jsonify(weather)
