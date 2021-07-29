# If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile),
#  then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again,
#  what time do I get home for breakfast?
import datetime

easy_pace = datetime.timedelta(minutes = 8, seconds = 15)
easy_miles = 2
tempo = datetime.timedelta(minutes = 7, seconds = 12)
tempo_miles = 3
run_time = (easy_pace * easy_miles) + (tempo * tempo_miles)
start_time = datetime.timedelta(hours = 6, minutes = 52)
breakfast_time = start_time + run_time
print(f"If you start running at {start_time}, you will be home for breakfast at {breakfast_time}!")

