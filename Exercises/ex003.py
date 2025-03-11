# Your Student ID: 230543001
# Your Name and Surname: Esra Gürbüz

import datetime

now = datetime.datetime.now()

print("Current date", now.date())
print("Current time", now.strftime("%H:%M:%S"))
print("Current date and time", now.strftime("%Y-%m-%d %H:%M:%S"))
