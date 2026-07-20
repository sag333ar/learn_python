import datetime
import camelcase

text = "hello world techcoderlabz sagar"
cci = camelcase.CamelCase()
print(cci.hump(text))

currentDate = datetime.datetime.now()

print(f"{currentDate.day}/{currentDate.month}/{currentDate.year}")
print(currentDate.strftime("%d/%m/%Y"))

year = 2026
month = 7
date = 10

myDate = datetime.datetime(year, month, date)
print(myDate)