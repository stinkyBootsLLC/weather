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
    """ Returns index.html (Jinja2 template engine)
        Passes variable data.

        Returns: render_template (render_template)
    """

    data = None

    if request.method == 'POST':

        
        # wrap with HTML escape
        zipcode = escape(request.form['zip-code'])

        

        state = escape(request.form['state'])

        city = escape(request.form['city'])

       

       

        if zipcode:

            data = get_weather(zipcode)

        else:

            data = get_weather(city, state)

    return render_template("index.html", data=data)


@app.context_processor
def utility_processor():
    """ injects new variables automatically into the context of a template

        Function get_day()
    """
    def get_day(date_str):
        """ Returns the day of the week based on a date string

            Parameters: date_str (str)
            Returns: Day (str)
        """

        date_format = '%Y-%m-%d %H:%M:%S'

        datetime_object = datetime.strptime(date_str, date_format)

        return datetime_object.strftime('%A')

    return dict(get_day=get_day)


if __name__ == "__main__":
    app.run(debug=True)
