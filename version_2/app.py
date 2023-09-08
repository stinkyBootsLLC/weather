from flask import Flask, render_template, request
from markupsafe import escape
from weather import main as get_weather

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

 

    if request.method == 'POST':
        # wrap with HTML escape
        zipcode = escape(request.form['zip-code'])

        data = get_weather(zipcode)

        print(data)

        # print(zipcode)
       
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
