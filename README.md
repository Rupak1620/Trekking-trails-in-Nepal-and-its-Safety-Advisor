# Nepal Trekking Weather Advisor

A Streamlit web application that provides real-time weather information and safety assessments for popular trekking routes in Nepal.

## Features

- Real-time weather data for popular trekking locations
- Safety assessments based on current weather conditions
- Altitude-specific weather simulations
- Customized recommendations for trekking safety
- User-friendly interface with interactive location selection

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/trekking-weather-advisor.git
cd trekking-weather-advisor
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the Streamlit app:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to the URL shown in the terminal (usually http://localhost:8501)

3. Select a trekking location from the dropdown menu to view:
   - Current weather conditions
   - Safety assessment
   - Trekking recommendations
   - Altitude-specific weather simulation

## Project Structure

- `app.py`: Main Streamlit application
- `weather_service.py`: Weather data service and safety assessment logic
- `requirements.txt`: Project dependencies
- `.gitignore`: Git ignore file

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- OpenWeatherMap API for weather data
- Streamlit for the web framework 