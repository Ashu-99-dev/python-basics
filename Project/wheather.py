import requests
from dotenv import load_dotenv
import os
from pprint import pprint
load_dotenv()
def get_current_weather():
    print('\n** Get Current weather conditions **\n')
    city = input('Please enter a city name: ')

    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'

    #print(request_url)\
    response = requests.get(request_url)
    data = response.json()
    #pprint(data)
    print(f"The current temperature in {city} is {data['main']['temp']}°C")
    print(f"The current humidity in {city} is {data['main']['humidity']}%")
    print(f"The current pressure in {city} is {data['main']['pressure']} hPa")
    print(f"The current wind speed in {city} is {data['wind']['speed']} m/s")
    print(f"The current weather in {city} is {data['weather'][0]['description']}")


if __name__ == '__main__':
    get_current_weather()

