import time  # This is required to include time module.

ticks = time.time()
print("Number of ticks since 12:00am, January 1, 1970:", ticks)

# ! Getting current time

localtime = time.localtime(time.time())
print("Local current time :", localtime)

# ! Getting formatted time
localtime = time.asctime(time.localtime(time.time()))
print("Local current time :", localtime)

# ! Getting calendar for a month
import calendar

cal = calendar.month(2021, 10)
print("Here is the calendar:")
print(cal)
