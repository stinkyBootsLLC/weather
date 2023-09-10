# Open-Weather-Py

Created for educational purposes only. I wanted to create a web app using the python flask framework.  I needed the application to be simple and cover the basics of using flask.  I created the original vers 1, to replace a html widget for a work project. It was a prototype and never implemented (I got a job somewhere else). I am currently in a dept. wide python training program (self pased) and working on seperate python projects not related to web technologies. This one was just for me and just for fun. This is a minimum viable application (very basic)

## Features

1. Search by U.S. zipcode.
2. Displays current weather
3. Displays five day weather forcast

### Dependencies

* Python 3.6.8
* Python Flask
* [openweathermap](https://openweathermap.org/) API key

### Installing

* Download or clone this repository

## Lessons Learned

This specific app would have been easier to create with just a javascript framework such as Node, Vue, etc...  It simply calls a rest API and renders the HTML.  So why did I use python? To learn.  The biggest problem, is that the app only searches by US zipcode. Users should be able to search weather by zipcode AND city name.  City names are much easier to memorize. State is not included in the JSON response. I have a free account, so it is limited. Seems like _"open weather"_ is click bait.

## Version History

* 2.0
    * Python Version
    * User input (zipcode only)
    * Python Version
    * Current weather
    * Five day forecast

* 1.0
    * Vanilla JavaScript
    * Single current weather widget for Tobyhanna PA only

## License

This project is licensed under the [The Unlicense](https://unlicense.org) 

## Acknowledgments

* [@datagy](https://youtu.be/JCD7YdOSsWI?si=8E_8CIXMRshxY1CK) Build YOUR OWN Weather App in Python with Flask (COMPLETE Beginner Tutorial)
* [Flask](https://flask.palletsprojects.com/en/2.3.x/) Documentation