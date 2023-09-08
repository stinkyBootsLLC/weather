from flask import Flask, render_template, request
from markupsafe import escape
from weather import main as get_weather

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

 
    data = None

    if request.method == 'POST':

        print(request.method)
        # wrap with HTML escape
        zipcode = escape(request.form['zip-code'])

        data = get_weather(zipcode)

        print(data)

        
       
    return render_template("index.html",data=data)


if __name__ == "__main__":
    app.run(debug=True)
