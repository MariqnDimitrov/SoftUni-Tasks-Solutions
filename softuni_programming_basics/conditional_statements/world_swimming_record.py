import math
record_seconds=float(input())
distance_meters=float(input())
time_seconds=float(input())
slowing_seconds=0
if distance_meters>=15:
    slowing=math.floor(distance_meters/15)
    slowing_seconds=slowing * 12.5
swimming_time=distance_meters * time_seconds + slowing_seconds
needed_seconds=abs(swimming_time - record_seconds)
if swimming_time>=record_seconds:
    print(f"No, he failed! He was {needed_seconds:.2f} seconds slower.")
else:
    print(f" Yes, he succeeded! The new world record is {swimming_time:.2f} seconds.")