""" 
Name: app.py
Description: Logic for flask web application
Author: Eduardo Estrada
Date: 9/10/2023
"""
from flask import Flask, render_template, request
from markupsafe import escape
from weather import main as get_weather
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    data = None

    if request.method == 'POST':

        print(request.method)
        # wrap with HTML escape
        zipcode = escape(request.form['zip-code'])

        if zipcode:

            data = get_weather(zipcode)

    return render_template("index.html", data=data)


@app.context_processor
def utility_processor():

    def get_day(date_str):

        date_format = '%Y-%m-%d %H:%M:%S'

        datetime_object = datetime.strptime(date_str, date_format)

        return datetime_object.strftime('%A')

    return dict(get_day=get_day)


if __name__ == "__main__":
    app.run(debug=True)
