""" 
Name: weather.py
Description: Logic for retrieving weather data form openweathermap.org RESTful API
Author: Eduardo Estrada
Date: 9/10/2023
"""
import config
import requests

def get_lat_and_long(zip_code): 
    """ Returns a list with lattitude and longitude coordinates 

        Parameters: zip_code (str)
        Returns: coordinates (list)
    """

    response = requests.get(f"https://api.openweathermap.org/geo/1.0/zip?zip={zip_code}&appid={config.api_key}").json()
    
    if 'cod' in response:

        coordinates = [response['cod'], response['message']]
    else:

        coordinates = [response['lat'], response['lon']]

    return coordinates 

def get_current_forcast(lat, long):

    """ Returns a dictionary of current weather information based on lattitude and longitude

        Parameters: lat, long (str)
        Returns: (dict)
    """

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

    """ Returns a list of 5 day weather forecast information based on lattitude and longitude

        Parameters: lat, long (str)
        Returns: response['list'] (list)
    """

    response = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={long}&units=imperial&appid={config.api_key}").json()

    return response['list']

def main(zip_code):

        """ Returns a dictionary of information based on zipcode

            Parameters: zip_code (str)
            Returns: weather_data (dict)
        """
    
    cordinates = get_lat_and_long(zip_code)
    
    if cordinates[0] != '404': 

        current_forcast = get_current_forcast(cordinates[0], cordinates[1])

        five_day_forcast = get_five_day_forcast(cordinates[0], cordinates[1])

        weather_data = {"current":current_forcast, "forcast":five_day_forcast }
    
    else:

        weather_data = {"Error":"coordinates failed"}

    return weather_data
 
    
if __name__ == "__main__":
   
    main(user_input)

 