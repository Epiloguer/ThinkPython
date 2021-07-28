# If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace
# (time per mile in minutes and seconds)? What is your average speed in miles per hour?

kilometers = 10
km_mi_conversion = 1.6
miles = kilometers * km_mi_conversion
print(f'you ran {miles} miles')
minutes = 42
minutes_to_seconds = minutes * 60
seconds = 42
total_seconds = minutes_to_seconds + seconds
print(f'in {total_seconds} seconds')
average_pace_seconds = miles/seconds
print(f'at a pace of {average_pace_seconds} miles per second')
average_pace_minutes = miles / (total_seconds / 60)
print(f'or at a pace of {average_pace_minutes} miles per minute')
