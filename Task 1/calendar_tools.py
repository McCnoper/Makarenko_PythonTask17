from datetime import datetime
from datetime import date
class UkrainianCalendar:
    def __init__(self):
        self.holidays = ["01-01","25-01","28-07","24-08"]
    def get_holiday_list():
        return self.holidays
    def is_working_day(self,date):
        day = date.weekday()
        print(day)
        date = date.strftime("%m-%d")
        if date in self.holidays or day >= 5:
            return False
        return True
