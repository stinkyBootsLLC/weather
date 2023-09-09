"""
Im going about this the wrong way

I need to define the functions of the app first

Then i have to use templates structure for flask
"""
import config
import requests

def get_lat_and_long(zip_code): 

    response = requests.get(f"https://api.openweathermap.org/geo/1.0/zip?zip={zip_code}&appid={config.api_key}").json()
    
    if 'cod' in response:

        coordinates = [response['cod'], response['message']]
    else:

         coordinates = [response['lat'], response['lon']]

    return coordinates 

def get_current_forcast(lat, long):

    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&units=imperial&appid={config.api_key}").json()
 
    return {
        "name":response["name"],
        "description":response["weather"][0]["description"],
        "icon":response["weather"][0]["icon"],
        "temp":response["main"]["temp"],
        "temp_min":response["main"]["temp_min"],
        "temp_max":response["main"]["temp_max"],
        "feels_like":response["main"]["feels_like"],
        "humidity":response["main"]["humidity"],
        "pressure":response["main"]["pressure"]
    }
 

def get_five_day_forcast(lat, long):
    response = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={long}&units=imperial&appid={config.api_key}").json()
    return response

def main(zip_code):
    
    cordinates = get_lat_and_long(zip_code)
    
    if cordinates[0] != '404': 

        current_forcast = get_current_forcast(cordinates[0], cordinates[1])
        # five_day_forcast = get_five_day_forcast(cordinates[0], cordinates[1])
    else:

        current_forcast = {"Error":"coordinates failed"}

    return current_forcast
 
    
if __name__ == "__main__":
   
    main(user_input)

 