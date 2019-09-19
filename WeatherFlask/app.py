from flask import Flask, request, render_template, make_response
from datetime import datetime
import json
import requests
import time
import atexit
import http.cookies

from apscheduler.schedulers.background import BackgroundScheduler

from api.ScheduleApi import ScheduleApi
from weather.GetWeather import GetWeather

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

@app.route('/class/<class_group>', methods=['GET', 'POST'])
def test(class_group):

    scheduleApi = ScheduleApi(class_group)
    getW = GetWeather()
    schedule_result = (scheduleApi.get_schedule_for_class_group())

    # Give HTML data to work with
    return render_template('MyTimetable.htm',
                           class_group = class_group,
                           result = schedule_result,
                           length = len(schedule_result),
                           weather = getW.weather10(),
                           weather_length = len(getW.weather10()['Date'])
                           )

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

