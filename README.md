# Weather Forecast

This is a simple weather forecast application that retrieves weather data for a given city using the OpenWeatherMap API. It displays information such as temperature, description, humidity, wind speed, and visibility.

## Prerequisites

Before running the application, make sure you have the following:

- Python 3.x installed
- OpenWeatherMap API key

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/weather-forecast.git
2. Install the required dependencies:
    ```bash
    pip install requests prettytable

3. Create a config.py file in the project directory and define your OpenWeatherMap API key:

    ```bash    
    # config.py
    api_key = "YOUR_API_KEY"
    url = "http://api.openweathermap.org/data/2.5/weather"

## Usage
1. Run the script:

    ```bash
    python weather_forecast.py
2. Enter the name of the city for which you want to get the weather forecast.

3. The weather information will be displayed in the terminal.

4. To exit the application, enter 'exit' when prompted for the city name.

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Contributing

Contributions are always welcome!

Please adhere to this project's `code of conduct`.
