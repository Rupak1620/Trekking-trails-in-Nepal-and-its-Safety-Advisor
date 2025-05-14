# Nepal Trekking Weather Advisor

A Streamlit web application that provides real-time weather information and safety assessments for popular trekking routes in Nepal.

## Features

- Real-time weather data for popular trekking locations
- Safety assessments based on current weather conditions
- Altitude-specific weather simulations
- Customized recommendations for trekking safety
- Packing list recommendations based on weather conditions

## Development Timeline

### Phase 1: Initial Development (January 2024)
- Project setup and basic architecture
- Integration with OpenWeatherMap API
- Basic weather data display functionality
- Initial UI design with Streamlit

### Phase 2: Core Features (February 2024)
- Implementation of safety assessment algorithms
- Altitude-specific weather simulations
- Basic trekking recommendations
- User interface improvements

### Phase 3: Enhanced Features (March 2024)
- Packing list recommendations
- Performance optimizations

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

4. Set up your environment variables:
```bash
# Create a .env file in the root directory
OPENWEATHERMAP_API_KEY=your_api_key_here
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
     
## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. Before contributing, please:

1. Fork the repository
2. Create a new branch for your feature
3. Make your changes
4. Submit a pull request

Please ensure your code follows PEP 8 style guidelines and includes appropriate tests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- OpenWeatherMap API for weather data
- Streamlit for the web framework
- Nepal Tourism Board for trekking route information
- Local trekking guides for safety recommendations 
