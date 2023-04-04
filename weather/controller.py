from weather.models import Weather
from app import db


class WeatherController:
    @staticmethod
    def create_weather(city, temperature, description):
        weather = Weather(city=city, temperature=temperature, description=description)
        db.session.add(weather)
        db.session.commit()
        return weather

    @staticmethod
    def get_all_weather():
        return Weather.query.all()
