import datetime

# python3 -m venv .venv
# source .venv/bin/activate
# python3 -m pip install camelcase
# run - `/Users/sagar/Desktop/learn_python/.venv/bin/python /Users/sagar/Desktop/learn_python/18_json_handling.py`

import camelcase

text = "hello world techcoderlabz sagar"
cci = camelcase.CamelCase()
print(cci.hump(text))

currentDate = datetime.datetime.now()
print(f"{currentDate.hour}:{currentDate.minute}, {currentDate.day}/{currentDate.month}/{currentDate.year}")
print(currentDate.strftime('%Y-%m-%d %H:%M %p'))
# Source - https://stackoverflow.com/a/1759498
# Posted by jamessan
# Retrieved 2026-07-27, License - CC BY-SA 2.5

format = '%Y-%m-%d %H:%M %p'


year = 2026
month = 7
date = 10

myDate = datetime.datetime(year, month, date)
print(myDate)