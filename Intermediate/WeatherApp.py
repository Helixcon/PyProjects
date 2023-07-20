import requests

API_KEY = "YOUR_API_KEY"  # Replace this with your OpenWeatherMap API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",  # For Celsius, change to "metric"; for Fahrenheit, use "imperial"
    }

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if data["cod"] == 200:
            weather_info = {
                "city": data["name"],
                "description": data["weather"][0]["description"],
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "wind_speed": data["wind"]["speed"],
            }
            return weather_info
        else:
            print("Error:", data["message"])
    except requests.exceptions.RequestException as e:
        print("Error connecting to the weather API:", e)

    return None

def display_weather(weather_info):
    if weather_info:
        print(f"Weather in {weather_info['city']}:")
        print(f"Description: {weather_info['description']}")
        print(f"Temperature: {weather_info['temperature']}°C")
        print(f"Humidity: {weather_info['humidity']}%")
        print(f"Wind Speed: {weather_info['wind_speed']} m/s")
    else:
        print("Weather information not available.")

def main():
    print("Welcome to the Weather App!")
    city = input("Enter the name of the city: ")

    weather_info = get_weather(city)

    display_weather(weather_info)

if __name__ == "__main__":
    main()
