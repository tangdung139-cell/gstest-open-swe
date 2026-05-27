import requests


def get_weather(city_name):
    """Fetch weather details for a city using OpenWeather API."""
    api_key = "your_api_key_here"  # Replace with your OpenWeather API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        weather_data = response.json()

        if weather_data.get("cod") != 200:
            print(f"Error: {weather_data.get('message', 'Unable to fetch weather data.')}")
            return

        weather_main = weather_data["weather"][0]["description"].capitalize()
        temperature = weather_data["main"]["temp"]

        print(f"Current weather in {city_name}: {weather_main}, {temperature}°C")

    except requests.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    city = input("Enter the city name: ")
    get_weather(city)
