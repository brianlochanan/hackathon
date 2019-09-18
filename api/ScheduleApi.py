from datetime import datetime, date
import requests
import json
from pytz import timezone
import calendar

class ScheduleApi:
    API_PATH = "https://rooster.hva.nl/m/api/timetable?start="+str(date.today())+"T00%3A00%3A00.000%2B02%3A00&limit=5&key=2019!studentset!FDMCI_IVMSFS"
    API_DATA_FORMAT = "&format=json"

    def __init__(self):
        pass

    def perform_request(self, path):
        session = requests.session()
        session.get("https://rooster.hva.nl/m")
        payload = {
            'JSESSIONID': session.cookies.get_dict()
        }

        request = session.get(self.API_PATH + path + self.API_DATA_FORMAT, params=payload)
        if request.status_code == 200:
            return json.loads(request.content)
        return None

    def get_api_path(self):
        return self.API_PATH

    def get_date_time_name(self, date):
        weekDay = calendar.day_name[datetime.fromtimestamp((int(str(date)[:-3]))).weekday()]
        dayNumber = datetime.fromtimestamp(int(str(date)[:-3])).strftime("%d")
        monthName = datetime.fromtimestamp(int(str(date)[:-3])).strftime("%B")
        year = datetime.fromtimestamp(int(str(date)[:-3])).strftime("%Y")
        dateTimeName = (str(weekDay + " " + dayNumber + " " + monthName + " " + year).lower())

        return dateTimeName

    def get_schedule_for_class_group(self):
        data = self.perform_request("")
        if 'data' not in data:
            print("No 'results' in json")
            return None

        schedule = []
        for timetable in data['data']:

            startTime = datetime.fromtimestamp(int(str(timetable['startDate'])[:-3])).strftime("%H:%M")
            endTime = datetime.fromtimestamp(int(str(timetable['endDate'])[:-3])).strftime("%H:%M")

            dateName = self.get_date_time_name(timetable['startDate'])

            weekNumber = (datetime.fromtimestamp(int(str(timetable['startDate'])[:-3])).strftime("%V"))

            schedule.append({
                'id': timetable['id'],
                'name': timetable['name'],
                'startTime': startTime,
                'endTime': endTime,
                'dateName': dateName,
                'weekNumber': weekNumber,
                'locations': timetable['locations']
            })

        return schedule