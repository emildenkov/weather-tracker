import requests


def from_kelvin_to_cel(temp):
    temp = int(temp)
    temp_in_cel = temp - 273.15
    return temp_in_cel


city_name = input('Enter valid name of city: ')
API_key = 'your API key'  # Site for API: Open Weather Map

url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units-metric'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"The description of the weather in {city_name} is :", data['weather'][0]['description'])
    real_temperature = data['main']['temp']
    feels_like = data['main']['feels_like']
    print(f"Temperature in {city_name} is: {from_kelvin_to_cel(real_temperature):.2f}, but it feels like: {from_kelvin_to_cel(feels_like):.2f}")
    print(f"The humidity in {city_name} is:", data['main']['humidity'])
else:
    raise ValueError("Incorrect city name!")

