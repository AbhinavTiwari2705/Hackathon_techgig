import requests as r
import config
from prettytable import PrettyTable

def get_weather(city):
    url = f"{config.url}?q={city}&appid={config.api_key}&units=metric"


    try:
        response = r.get(url)
        response.raise_for_status()

        weather_data = response.json()

        temperature = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        visibility = weather_data['visibility']

        table = PrettyTable()
        table.field_names = ["Details", "Results"]
        table.add_row(["City", city])
        table.add_row(["Temperature", f"{temperature}°C"])
        table.add_row(["Description", description])
        table.add_row(["Humidity", f"{humidity}%"])
        table.add_row(["Wind Speed", f"{wind_speed} m/s"])
        table.add_row(["Visibility", f"{visibility} m"])

        print()
        print("╔══════════════════════════════════╗")
        print("║                                  ║")
        print("║          Weather Forecast        ║")
        print("║                                  ║")
        print("╚══════════════════════════════════╝")
        print(table.get_string(title="Weather Forecast")) #used copilot here
        print()

    except r.exceptions.RequestException as e:
        print(f"Could not get weather data for {city}")
    except KeyError:
        print("Invalid response received from the API. Please try again.")

if __name__ == "__main__":
    while True:
        city_name = input("Enter the name of the city (or 'exit' to quit): ")
        if city_name == "exit":   #used copilot here
            break
        get_weather(city_name)
