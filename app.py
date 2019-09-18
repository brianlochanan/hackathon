from flask import Flask, request, render_template, jsonify
import json
import requests
import time
import atexit

from apscheduler.schedulers.background import BackgroundScheduler

from api.ScheduleApi import ScheduleApi

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

"""
@app.route('/class/<class_group>', methods=['GET'])
def test(class_group):
    scheduleApi = ScheduleApi()
    print(scheduleApi.get_schedule_for_class_group())
    return render_template('MyTimetable.htm', class_group = class_group)
"""

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



@app.route('/getWeather', methods=['GET','POST'])
def get_weather():
    start_h = request.args.get('start_h')
    start_d = request.args.get('start_d')
    end_h = request.args.get('end_h')
    end_d = request.args.get('end_d')
    start = start_d + " " + start_h
    end = end_d + " " + end_h
    #print(start)

    with open("weather.txt") as f:
        data = json.load(f)

    for row in data['data']:
        print(row['tijd_nl'])
        print(start)
        print(end)
        print()
        if(row['tijd_nl'] == start):
            start_temp = row['temp']
            start_wind = row['winds']
            start_neersl = row['neersl']
            print("start")

        elif(row['tijd_nl'] == end):
            end_temp = row['temp']
            end_wind = row['winds']
            end_neersl = row['neersl']
            print("end")

    try:

        r = [
                    {
                        "temp": start_temp,
                        "winds": start_wind,
                        "neersl": start_neersl,
                    },
                    {
                        "temp": end_temp,
                        "winds": end_wind,
                        "neersl": end_neersl,
                    },
                ]
        return jsonify(results = r)
    except:
        return "Error in parameters"


if __name__ == '__main__':
    app.run()

