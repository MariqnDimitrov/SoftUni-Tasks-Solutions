hours=int(input())
minutes=int(input())
minutes_ahead=minutes+15
if minutes_ahead>=60:
    hours=hours+1
    minutes_ahead=minutes_ahead - 60
if hours>=24:
    hours=0
if minutes_ahead<10:
    print(f"{hours}:0{minutes_ahead}")
else:
    print(f"{hours}:{minutes_ahead}")