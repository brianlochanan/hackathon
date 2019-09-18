import calendar
from datetime import datetime

class DateTimeService:

    def __init__(self):
        pass

    # Concatenate weekday name, daynumber of the month, monthname and year
    def get_date_time_name(self, date):
        weekDay = calendar.day_name[datetime.fromtimestamp((int(str(date)[:-3]))).weekday()]
        dayNumber = datetime.fromtimestamp(int(str(date)[:-3])).strftime("%d")
        monthName = datetime.fromtimestamp(int(str(date)[:-3])).strftime("%B")
        year = datetime.fromtimestamp(int(str(date)[:-3])).strftime("%Y")
        dateTimeName = (str(weekDay + " " + dayNumber + " " + monthName + " " + year).lower())

        return dateTimeName