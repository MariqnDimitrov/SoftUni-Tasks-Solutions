import math
serial_name=input()
time_episode=int(input())
time_break=int(input())
lunch_time=time_break/8
relax_time=time_break/4
serial_time=time_break - lunch_time - relax_time
time_left=math.ceil(abs(serial_time - time_episode))
if serial_time>=time_episode:
    print(f"You have enough time to watch {serial_name} and left with {time_left} minutes free time.")
else:
    print(f"You don't have enough time to watch {serial_name}, you need {time_left} more minutes.")