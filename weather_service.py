import os
import requests
from typing import Dict
import random
from datetime import datetime

class WeatherService:
    def __init__(self):
        self.api_key = "fca52fda8bbd179494352b9405ea7370"
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"  # Changed to https
        self.base_conditions = {
            'spring': {'temp_range': (5, 15), 'wind_range': (5, 15), 'conditions': ['Clear', 'Clouds', 'Rain']},
            'summer': {'temp_range': (10, 20), 'wind_range': (3, 12), 'conditions': ['Clear', 'Clouds', 'Rain', 'Thunderstorm']},
            'autumn': {'temp_range': (0, 10), 'wind_range': (8, 20), 'conditions': ['Clear', 'Clouds', 'Snow']},
            'winter': {'temp_range': (-15, 0), 'wind_range': (10, 25), 'conditions': ['Clear', 'Clouds', 'Snow', 'Blizzard']}
        }
        
    def _get_current_season(self) -> str:
        """Determine season based on current month."""
        month = datetime.now().month
        if month in [3, 4, 5]:
            return 'spring'
        elif month in [6, 7, 8]:
            return 'summer'
        elif month in [9, 10, 11]:
            return 'autumn'
        else:
            return 'winter'
            
    def _generate_weather_data(self, altitude: float) -> Dict:
        """Generate realistic weather data based on altitude and season."""
        season = self._get_current_season()
        conditions = self.base_conditions[season]
        
        # Adjust temperature based on altitude (roughly -6.5°C per 1000m)
        altitude_effect = (altitude - 1000) * -0.0065
        temp_min, temp_max = conditions['temp_range']
        temp = random.uniform(temp_min, temp_max) + altitude_effect
        
        # Adjust wind based on altitude (increases with height)
        wind_min, wind_max = conditions['wind_range']
        wind_factor = 1 + (altitude / 5000)
        wind = random.uniform(wind_min, wind_max) * wind_factor
        
        weather_main = random.choice(conditions['conditions'])
        
        return {
            'weather': [{'main': weather_main}],
            'main': {'temp': round(temp, 1)},
            'wind': {'speed': round(wind, 1)}
        }
        
    def get_weather_data(self, latitude: float, longitude: float) -> Dict:
        """Fetch current weather data for given coordinates."""
        params = {
            'lat': latitude,
            'lon': longitude,
            'appid': self.api_key,
            'units': 'metric'  # Use metric units for temperature
        }
        
        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()  # This will raise an exception for error status codes
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching weather data: {e}")
            return {}
            
    def get_safety_impact(self, weather_data: Dict) -> str:
        """Analyze weather conditions and return safety impact level."""
        if not weather_data:
            return "Unknown"
            
        # Extract relevant weather parameters
        temp = weather_data.get('main', {}).get('temp', 0)
        wind_speed = weather_data.get('wind', {}).get('speed', 0)
        weather_main = weather_data.get('weather', [{}])[0].get('main', '')
        
        # Basic safety assessment
        if weather_main in ['Thunderstorm', 'Blizzard'] or temp < -20 or wind_speed > 25:
            return "High Risk"
        elif weather_main in ['Snow', 'Heavy Rain'] or temp < -10 or wind_speed > 20:
            return "Moderate Risk"
        else:
            return "Safe"
            
    def get_weather_summary(self, weather_data: Dict) -> str:
        """Generate a human-readable weather summary."""
        if not weather_data:
            return "Weather data unavailable"
            
        main = weather_data.get('weather', [{}])[0].get('main', 'Unknown')
        temp = weather_data.get('main', {}).get('temp', 0)
        wind = weather_data.get('wind', {}).get('speed', 0)
        
        return f"Current Conditions: {main}, Temperature: {temp}°C, Wind Speed: {wind} m/s"

def main():
    # Example usage
    service = WeatherService()
    # Example coordinates for Everest Base Camp
    weather_data = service.get_weather_data(27.9881, 86.9250)
    print("\nWeather Data:")
    print(weather_data)
    print("\nSafety Impact:")
    print(service.get_safety_impact(weather_data))
    print("\nWeather Summary:")
    print(service.get_weather_summary(weather_data))

if __name__ == "__main__":
    main() 