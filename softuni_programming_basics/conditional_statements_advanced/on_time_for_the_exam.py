exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

exam_time_minutes = exam_hour * 60 + exam_minutes

arrival_time_minutes = arrival_hour * 60 + arrival_minute

diff_min = abs(exam_time_minutes - arrival_time_minutes)
diff_hour = diff_min//60

if exam_time_minutes < arrival_time_minutes:
    print("Late")

    if diff_min < 60:
        print(f"{diff_min} minutes after the start")

    elif diff_min >= 60:
        diff_min = diff_min % 60

        if diff_min < 10:
            print(f"{diff_hour}:0{diff_min} hours after the start")

        else:
            print(f"{diff_hour}:{diff_min} hours after the start")

elif exam_time_minutes == arrival_time_minutes or diff_min <= 30:
    print("On time")

    if 60 > diff_min > 0 and exam_time_minutes > arrival_time_minutes:
        print(f"{diff_min} minutes before the start")
else:
    print("Early")

    if diff_min >= 60:
        diff_min = diff_min % 60

        if 9 < diff_min < 60:
            print(f"{diff_hour}:{diff_min} hours before the start")

        elif diff_min < 10:
            print(f"{diff_hour}:0{diff_min} hours before the start")
    else:
        print(f"{diff_min} minutes before the start")