from flask import Flask, request
import json
import requests
import time
import atexit

from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)


def request_and_save_weather_data():

    params = (
        ('locatie', 'Amsterdam'),
        ('key', '85c9b987c6'),
    )

    response = requests.get('https://meteoserver.nl/api/uurverwachting.php', params=params)
    content = response.content

    file = open("weather.txt", "w+")
    file.write(str(response.content)[2:-1])
    print('wrote new weather data file')


# initiate scheduler for retrieving weather data
scheduler = BackgroundScheduler()
scheduler.add_job(func=request_and_save_weather_data, trigger="interval", hours=1)
scheduler.start()

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())

# this route should return the home page. i.e. the recommendation on what to wear
@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello World!'

@app.route('/<class_group>')
def class_group(class_group):
   return render_template('/MyTimetable.htm', class_group = class_group)

# not sure if we need this
@app.route('/city')
def show_city():
    with open("weather.txt") as f:
        data = json.load(f)

    return data['plaatsnaam'][0]["plaats"]

@app.route('/addCourse', methods=['GET','POST'])
def add_course():
    if request.method == 'GET':
        """show interface for adding courses"""
        return
    if request.method == 'POST':
        """read post attribute and use that to store time data in cookie"""
        return




if __name__ == '__main__':
    app.run()

