from datetime import datetime, date
from DateTimeService.DateTimeService import DateTimeService
import requests
import json

class ScheduleApi:

    class_group = ""
    API_PATH = "https://rooster.hva.nl/m/api/timetable?start="+str(date.today())+"T00%3A00%3A00.000%2B02%3A00&limit=10&key="
    API_DATA_FORMAT = "&format=json"
    GET_CLASS = "https://rooster.hva.nl/m/api/search/timetables?q="

    def __init__(self, class_group):
        self.class_group = class_group
        pass

    def perform_request(self, path):

        # Set cookie to authorize the program to use the timetable API
        session = requests.session()
        session.get("https://rooster.hva.nl/m")
        payload = {
            'JSESSIONID': session.cookies.get_dict()
        }

        # Request student set by searching class
        get_class = session.get(self.GET_CLASS + path +
                                "&subscriptionGroup="+ str(datetime.now().year) +
                                "&type=studentset&limit=50" + self.API_DATA_FORMAT, params=payload)

        # Get student class
        student_set = ""
        if get_class.status_code == 200:
            class_json = json.loads(get_class.content)
            student_set = class_json['data'][0]['key']

        # Request timetable API for student set
        request = session.get(self.API_PATH + student_set + self.API_DATA_FORMAT, params=payload)
        if request.status_code == 200:
            return json.loads(request.content)
        return None

    def get_api_path(self):
        return self.API_PATH

    def get_schedule_for_class_group(self):
        data = self.perform_request(self.class_group)
        if 'data' not in data:
            print("No 'results' in json")
            return None

        dateTimeService = DateTimeService()
        schedule = []
        for timetable in data['data']:

            # Get specific datetime for comparing with weather datetime
            timeTableStartDate = datetime.fromtimestamp(int(str(timetable['startDate'])[:-3])).strftime("%d-%m-%Y %H:00")
            timeTableEndDate = datetime.fromtimestamp(int(str(timetable['endDate'])[:-3])).strftime(
                "%d-%m-%Y %H:00")

            startTime = datetime.fromtimestamp(int(str(timetable['startDate'])[:-3])).strftime("%H:%M")
            endTime = datetime.fromtimestamp(int(str(timetable['endDate'])[:-3])).strftime("%H:%M")

            dateName = dateTimeService.get_date_time_name(timetable['startDate'])
            weekNumber = (datetime.fromtimestamp(int(str(timetable['startDate'])[:-3])).strftime("%V"))

            schedule.append({
                'id': timetable['id'],
                'name': timetable['name'],
                'startTime': startTime,
                'endTime': endTime,
                'dateName': dateName,
                'weekNumber': weekNumber,
                'timeTableStartDate': timeTableStartDate,
                'timeTableEndDate': timeTableEndDate,
                'locations': timetable['locations']
            })

        return schedule