first_competitor=int(input())
second_competitor=int(input())
third_competitor=int(input())
time_sum=first_competitor + second_competitor + third_competitor
minutes=time_sum//60
seconds=time_sum%60
if seconds<=9:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")