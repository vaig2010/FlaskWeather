from weatherController import getCityWeather
from flask import Flask, render_template, request
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=['GET', 'POST'])
def index():
    city = 'Moscow'
    if request.method == 'POST':
        city = request.form.get('city')
    weather = getCityWeather(city)
    return render_template('weather.html', weather=weather)
