from typing import final
import requests  
from pprint import pprint
API_Key="7c24cb0bd9a0fe2a987bd793550192f8"
location=input("Enter Your Desired Location: ")
weather_url=f"http://api.openweathermap.org/data/2.5/weather? q={location} &appid="
final_url=weather_url+API_Key
weather_data=requests.get(final_url).json()
pprint(weather_data)