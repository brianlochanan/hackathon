from datetime import date
import requests
import json

class ScheduleApi:
    API_PATH = "https://rooster.hva.nl/m/api/timetable?start=2019-09-17T00%3A00%3A00.000%2B02%3A00&limit=25&key=2019!studentset!FDMCI_IVMSFS"
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

    def get_schedule_for_class_group(self):
        data = self.perform_request("")
        if 'data' not in data:
            print("No 'results' in json")
            return None

        schedule = []
        for schedule in data['data']:

            #print schedule
            print(schedule)
            # schedule.append({
            #     'id': schedule['id'],
            #     'name': schedule['_display'],
            #     'type': schedule['waste_name'],
            #     'address': schedule['address'],
            # })

        # return trash_bins