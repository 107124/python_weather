import requests
import ast

url = "https://community-open-weather-map.p.rapidapi.com/forecast"

city = input("Type in a city:\n")
querystring = {"q":f"{city},us"}

headers = {
    'x-rapidapi-key': "7603016162msh8263f88a5aa10dfp18e91ajsna3493aef8fcf",
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

text_response = ast.literal_eval(response.text)

main = text_response["list"][0]["main"]
weather = text_response["list"][0]["weather"]
wind = text_response["list"][0]["wind"]

def convert_temp(temp):
    new_temp = round(((temp - 273.15) * (9 / 5) + 32), 2)
    return(new_temp)

data = {
    "City": city.title(),
    "sky": weather[0]["description"],
    "temp": f"{convert_temp(main['temp'])}° F",
    "today's high": f"{convert_temp(main['temp_max'])}° F",
    "today's low": f"{convert_temp(main['temp_min'])}° F",
    "wind speed": f"{wind['speed']} mph",
    "wind gust": f"{wind['gust']} mph",

}

for key, value in data.items():
    print(f"{key.title()}: {value}")





