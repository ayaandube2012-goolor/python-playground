import datetime as dt
import smtplib

now = dt.datetime
day = now.weekday()
print(day)
if day == 0:
    pass
