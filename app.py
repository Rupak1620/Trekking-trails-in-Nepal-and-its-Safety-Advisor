import streamlit as st
from weather_service import WeatherService
import pandas as pd

service = WeatherService()

st.set_page_config(
    page_title="Nepal Trekking Weather Advisor",
    page_icon="⛰️",
    layout="wide"
)

st.title("⛰️ Nepal Trekking Weather Advisor")
st.markdown("""
This app provides real-time weather information and safety assessments for popular trekking routes in Nepal.
Select a location to get current weather conditions and safety recommendations.
""")

locations = {
    "Everest Base Camp": {"lat": 27.9881, "lon": 86.9250, "altitude": 5364},
    "Annapurna Base Camp": {"lat": 28.5500, "lon": 83.8167, "altitude": 4130},
    "Langtang Valley": {"lat": 28.2000, "lon": 85.5000, "altitude": 3500},
    "Manaslu Circuit": {"lat": 28.5500, "lon": 84.5500, "altitude": 5106}
}

col1, col2 = st.columns([1, 2])

with col1:
    selected_location = st.selectbox(
        "Select Trekking Location",
        list(locations.keys())
    )
    
    location_info = locations[selected_location]
    
    st.subheader("Location Details")
    st.write(f"Altitude: {location_info['altitude']}m")
    st.write(f"Coordinates: {location_info['lat']}°N, {location_info['lon']}°E")

with col2:
    weather_data = service.get_weather_data(location_info['lat'], location_info['lon'])
    
    if weather_data:
        st.subheader("Current Weather Conditions")
        
        col_temp, col_wind, col_humidity = st.columns(3)
        
        with col_temp:
            temp = weather_data.get('main', {}).get('temp', 0)
            st.metric("Temperature", f"{temp}°C")
        
        with col_wind:
            wind = weather_data.get('wind', {}).get('speed', 0)
            st.metric("Wind Speed", f"{wind} m/s")
        
        with col_humidity:
            humidity = weather_data.get('main', {}).get('humidity', 0)
            st.metric("Humidity", f"{humidity}%")
        
        weather_desc = weather_data.get('weather', [{}])[0].get('description', '')
        st.write(f"Weather: {weather_desc}")
        
        safety = service.get_safety_impact(weather_data)
        st.subheader("Safety Assessment")
        
        if safety == "High Risk":
            st.error("⚠️ HIGH RISK: Consider postponing trek or taking extra precautions")
        elif safety == "Moderate Risk":
            st.warning("⚠️ MODERATE RISK: Proceed with caution and proper equipment")
        else:
            st.success("✅ SAFE: Standard precautions advised")
        
        st.subheader("Recommendations")
        if temp < -10:
            st.write("❄️ Wear thermal layers and proper cold-weather gear")
        if wind > 15:
            st.write("💨 Be cautious of strong winds, especially on exposed ridges")
        if weather_desc.lower().find('rain') != -1 or weather_desc.lower().find('snow') != -1:
            st.write("🌧️ Bring waterproof gear and be prepared for slippery conditions")
        
        st.subheader("Altitude-Specific Weather Simulation")
        simulated_data = service._generate_weather_data(location_info['altitude'])
        st.write(service.get_weather_summary(simulated_data))
    else:
        st.error("Unable to fetch weather data. Please try again later.")

st.markdown("---")
st.markdown("""
*Note: This is a safety advisory tool. Always check with local authorities and guides before trekking.*
""")