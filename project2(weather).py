import requests
import json
import pyttsx3
engine = pyttsx3.init() 

while True:
    city = input("Enter your city name :")

    url = f"https://api.weatherapi.com/v1/current.json?key=7dd5c03dccf440b193c60846241609&q={city}"
    r = requests.get(url)
    weather_dic = json.loads(r.text)
    Temperature = weather_dic["current"]["temp_c"]

     
    engine.say(f"The current Weather  in: {city} is :{Temperature}")  


    engine.runAndWait() 
