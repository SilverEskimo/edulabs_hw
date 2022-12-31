#Q11:
total_secs = int(input("Please enter the length of the movie in seconds: "))
total_mins = total_secs // 60
res_seconds = total_secs % 60
res_minutes = total_mins % 60
res_hours = total_mins // 60

print(f'{res_hours}:{res_minutes}:{res_seconds}')