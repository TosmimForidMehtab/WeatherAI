import requests
import config

API_KEY = config.API_KEY
BASE_URL = config.BASE_URL
def getWeather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        "units": "metric",
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weatherDesc = data['weather'][0]['description']
        temp = main['temp']
        humidity = main['humidity']
        return f"The weather in {city} is currently {weatherDesc}. The temperature is {temp} degrees Celsius and the humidity is {humidity} percent." 
    
    else:
        return f"Failed to retrieve weather for {city}.Please try again later."

if __name__ == '__main__':
    print(getWeather('Mumbai'))