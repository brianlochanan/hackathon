from flask import Flask, request, render_template, redirect
import requests
import atexit

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from apscheduler.schedulers.background import BackgroundScheduler

from api.ScheduleApi import ScheduleApi
from weather.GetWeather import GetWeather

app = Flask(__name__)


def request_and_save_weather_data():
    params = (
        ('locatie', 'Amsterdam'),
        ('key', 'a1c65a55b9'),
    )

    response = requests.get('https://meteoserver.nl/api/uurverwachting_gfs.php', params=params)
    content = response.content

    file = open("weather10.txt", "w+")
    file.write(str(response.content)[2:-1])
    print('wrote new weather data file')


# initiate scheduler for retrieving weather data
scheduler = BackgroundScheduler()
scheduler.add_job(func=request_and_save_weather_data, trigger="interval", hours=1)
scheduler.start()

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())


# this route should return the home page. i.e. the recommendation on what to wear
@app.route('/', methods=['GET', 'POST'])
def selectCourse():
    # x = input('Add the first leters of your course')
    # return redirect('/class/' + x)
    if request.method == 'POST':
        course = request.form['Course']
        print(course)
        return redirect('/class/' + course)

    # Give HTML data to work with
    return render_template('SelectCourse.html')


@app.route('/class/<class_group>', methods=['GET', 'POST'])
def test(class_group):
    scheduleApi = ScheduleApi(class_group)
    getW = GetWeather()
    schedule_result = (scheduleApi.get_schedule_for_class_group())

    # Give HTML data to work with
    return render_template('MyTimetable.htm',
                           class_group=class_group,
                           result=schedule_result,
                           length=len(schedule_result),
                           weather=getW.weather10(),
                           weather_length=len(getW.weather10()['Date'])
                           )


if __name__ == '__main__':
    app.run()
