"""
Im going about this the wrong way

I need to define the functions of the app first

Then i have to use templates structure for flask
"""
import config
import requests

def get_lat_and_long(zip_code): 

    response = requests.get(f"https://api.openweathermap.org/geo/1.0/zip?zip={zip_code}&appid={config.api_key}").json()

    return [response["lat"], response["lon"]]

def get_current_forcast(lat, long):

    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&units=imperial&appid={config.api_key}").json()
    return {
        "description":response["weather"][0]["description"],
        "icon":response["weather"][0]["icon"],
        "temp":response["main"]["temp"],
        "temp_min":response["main"]["temp_min"],
        "temp_max":response["main"]["temp_max"],
        "feels_like":response["main"]["feels_like"],
        "humidity":response["main"]["humidity"]
    }
 

   
     
     

def get_five_day_forcast(lat, long):
    response = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={long}&units=imperial&appid={config.api_key}").json()
    return response

cordinates = get_lat_and_long("18062")
# print(cordinates)

current_forcast = get_current_forcast(cordinates[0], cordinates[1])
print(current_forcast)

five_day_forcast = get_five_day_forcast(cordinates[0], cordinates[1])
# print(five_day_forcast)