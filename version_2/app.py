from flask import Flask

import os, requests, config

app = Flask(__name__)

@app.route('/', methods =['GET'])
def index():
    location_url = f"https://api.openweathermap.org/geo/1.0/zip?zip=18062&appid={config.api_key}"
    location_response = requests.get(location_url)

    list_of_data = location_response.json()

    html_data = f"""
        <input type="text" placeholder="Search this shiat.."> 
        <table border="1">
        <tr>
            <td>Zip</td>
            <td>Name</td>
            <td>Lat</td>
            <td>Long</td>
            <td>Country</td>
        </tr>
        <tr>
            <td>{str(list_of_data['zip'])}</td>
            <td>{str(list_of_data['name'])}</td>
            <td>{str(list_of_data['lat'])}</td>
            <td>{str(list_of_data['lon'])}</td>
            <td>{str(list_of_data['country'])}</td>
        </tr>

        </table>
    """


  

    return html_data


 