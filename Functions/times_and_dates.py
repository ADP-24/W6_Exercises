import datetime

today = datetime.datetime.now()

formatted_date= today.strftime("Today is %A, %B, %d, %Y")

print(formatted_date)

birthday = datetime.date(1995, 1, 4)

formatted_birthday = birthday.strftime("My birthday is %m/%d/%Y")

print(formatted_birthday)

today = datetime.datetime.now().date()

ninety_d = today + datetime.timedelta(days=90)

print("The date 90 days from today is:", ninety_d)

import datetime

dinner_time = datetime.time(19,30)

formatted_dinner_time = dinner_time.strftime("Let's meet for dinner at %I:%M %p")

print(formatted_dinner_time)