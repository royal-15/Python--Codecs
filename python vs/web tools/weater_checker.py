import requests as r
from bs4 import BeautifulSoup as bs

apikey = "5ff797396f14c6afff84f00746bd4654"

url = f"http://api.openweathermap.org/data/2.5/weather?"

while True:    
    city_name = input("Enter city name for weather enquiry: ")
    if city_name == "0":
        break
    
    main_url = url+"appid="+apikey+"&q="+city_name

    weather_stats = r.get(main_url).json()

    if weather_stats["cod"]=="404":
        print("City not Found!")
        exit()

    main = weather_stats["main"]
    # Extracting vlaues from main
    temprature =  main["temp"] - 273.15
    pressure = main["pressure"]
    humidity = main["humidity"]

    # Extracting values from weather_stats
    weather = weather_stats["weather"]

    # Extracting values from weather
    weather_description = weather[0]["description"]

    print(f"Temprature = {str(temprature)}\nAtmospheric Pressure = {str(pressure)}\nHumidity = {str(humidity)}\nDescription = {str(weather_description)}")