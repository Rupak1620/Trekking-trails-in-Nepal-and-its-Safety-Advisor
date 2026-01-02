from weather_service import WeatherService
import time

def test_trekking_scenarios():
    service = WeatherService()
    
    # Popular trekking locations in Nepal
    locations = {
        "Everest Base Camp": {"lat": 27.9881, "lon": 86.9250, "altitude": 5364},
        "Annapurna Base Camp": {"lat": 28.5500, "lon": 83.8167, "altitude": 4130},
        "Langtang Valley": {"lat": 28.2000, "lon": 85.5000, "altitude": 3500},
        "Manaslu Circuit": {"lat": 28.5500, "lon": 84.5500, "altitude": 5106}
    }
    
    print("\n=== Trekking Weather Safety Assessment ===")
    print("Testing weather conditions for popular trekking routes in Nepal...\n")
    
    for location, info in locations.items():
        print(f"\nLocation: {location}")
        print(f"Altitude: {info['altitude']}m")
        
        weather_data = service.get_weather_data(info['lat'], info['lon'])
        
        if weather_data:
            safety = service.get_safety_impact(weather_data)
            summary = service.get_weather_summary(weather_data)
            
            print("\nCurrent Weather Conditions:")
            print(summary)
            print(f"Safety Assessment: {safety}")
            simulated_data = service._generate_weather_data(info['altitude'])
            simulated_safety = service.get_safety_impact(simulated_data)
            print("\nSimulated Weather for this Altitude:")
            print(service.get_weather_summary(simulated_data))
            print(f"Simulated Safety Assessment: {simulated_safety}")
            
            if safety == "High Risk":
                print("\n⚠️ WARNING: High risk conditions detected!")
                print("Recommendation: Consider postponing trek or taking extra precautions")
            elif safety == "Moderate Risk":
                print("\n⚠️ CAUTION: Moderate risk conditions")
                print("Recommendation: Proceed with caution and proper equipment")
            else:
                print("\n✅ Conditions are generally safe for trekking")
                print("Recommendation: Standard precautions advised")
                
            print("\n" + "="*50)
            time.sleep(2)
        else:
            print("Error: Could not fetch weather data for this location")

if __name__ == "__main__":
    test_trekking_scenarios() 
