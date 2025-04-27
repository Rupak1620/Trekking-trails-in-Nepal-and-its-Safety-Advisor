import requests
import json

def test_api():
    api_key = "fca52fda8bbd179494352b9405ea7370"
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    
    # Test locations
    locations = {
        "Kathmandu": {"lat": 27.7172, "lon": 85.3240},
        "Everest Base Camp": {"lat": 27.9881, "lon": 86.9250},
        "Pokhara": {"lat": 28.2097, "lon": 83.9856},
        "Annapurna Base Camp": {"lat": 28.5500, "lon": 83.8167}
    }
    
    for location, coords in locations.items():
        print(f"\nTesting {location}...")
        params = {
            'lat': coords['lat'],
            'lon': coords['lon'],
            'appid': api_key,
            'units': 'metric'
        }
        
        try:
            response = requests.get(base_url, params=params)
            print(f"Status Code: {response.status_code}")
            
            if response.status_code == 200:
                data = response.json()
                print(f"Location: {data.get('name', 'Unknown')}")
                print(f"Temperature: {data.get('main', {}).get('temp', 'N/A')}°C")
                print(f"Weather: {data.get('weather', [{}])[0].get('main', 'Unknown')}")
                print(f"Wind Speed: {data.get('wind', {}).get('speed', 'N/A')} m/s")
            else:
                print(f"Error: {response.text}")
                
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    test_api() 