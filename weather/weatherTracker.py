from urllib import response
import requests
API_KEY = "73ba7c7ca5fbd5bde79ba42b167c03c2"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city: ")
request_url = f"{BASE_URL}?q={city}&units=imperial&appid={API_KEY}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    #newprint(data)
    weather = data['weather'][0]["description"]
    print(f"Weather is {weather}.")
    temp = data['main']["temp"]
    print(f"Temperature: {temp}F.")
else:
    print("Error occured during API call.")
