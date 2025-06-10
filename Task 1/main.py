from calendar_tools import UkrainianCalendar
from datetime import date
calendar = UkrainianCalendar()
print(calendar.holidays)
test_date=[date(2025,1,1),
           date(2025,2,3)]
for d in test_date:
    if calendar.is_working_day(d):
        print("Робочий")
    else:
        print("Свято")
