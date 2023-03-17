"""
Project: Weather Forecasting Application

The aim of this project is to build a weather forecasting application
that uses data from an API to provide weather information to the user.
The application should be able to display the temperature, humidity, wind speed,
and other relevant information based on the user's location or
any other location specified by the user.
"""

import requests


def get_weather_data(api_key, location):
    """
    This function retrieves the weather data from the API
    """
    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def display_weather_data(weather_data):
    """
    This function displays the weather data to the user
    """
    if weather_data is not None:
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]
        description = weather_data["weather"][0]["description"]
        print(f"Temperature: {temperature} K")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Description: {description}")
    else:
        print("Unable to retrieve weather data")


# Main function
def main():
    api_key = "API_KEY"
    location = input("Enter the name of the location: ")
    weather_data = get_weather_data(api_key, location)
    display_weather_data(weather_data)


if __name__ == "__main__":
    main()


