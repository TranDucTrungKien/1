def format_time(t):
    hour = (t // 3600) % 24
    minute = (t % 3600) // 60
    second = (t % 3600) % 60
    period = "AM" if hour < 12 else "PM"
    hour = hour % 12
    hour = 12 if hour == 0 else hour
    return f"{hour}:{minute:02}:{second:02} {period}"
try:
    t = int(input("Enter the number of seconds: "))
    formatted_time = format_time(t)
    print(formatted_time)
except ValueError:
    print("Please enter a valid integer for seconds.")