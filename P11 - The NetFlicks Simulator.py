times = input().split(", ")
total_time = times[0]
total_time = total_time.split(":")
total_minutes = int(total_time[0])*60+int(total_time[1])
times.pop(0)
real_times = None
if len(times) > 7:
    real_times = times[0:6]
else:
    real_times = times
for i in real_times:
    i = i.split(":")
    i = int(i[0])*60 + int(i[1])
    total_minutes -= i

if total_minutes >= 0:
    remaining_hours = int(total_minutes/60)
    remaining_minutes = str(total_minutes-remaining_hours*60)
    remaining_hours = str(remaining_hours)
    if len(remaining_hours) == 1:
        remaining_hours = "0" + remaining_hours
    if len(remaining_minutes) == 1:
        remaining_minutes = "0" + remaining_minutes
    remaining = str(remaining_hours) + ":" + remaining_minutes
    print(remaining + " hours of viewing remaining.")

if total_minutes < 0:
    total_minutes = -total_minutes
    remaining_hours = int(total_minutes/60)
    remaining_minutes = str(total_minutes-remaining_hours*60)
    remaining_hours = str(remaining_hours)
    if len(remaining_hours) == 1:
        remaining_hours = "0" + remaining_hours
    if len(remaining_minutes) == 1:
        remaining_minutes = "0" + remaining_minutes
    remaining = str(remaining_hours) + ":" + remaining_minutes
    print("LIMIT EXCEEDED BY " + remaining + " hours. Benigno punished!")
