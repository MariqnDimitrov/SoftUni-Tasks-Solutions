numbers= int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
for i in range(1,numbers + 1):
    current_num = int(input())
    if current_num < 200:
        p1 = p1 + 1
    elif 200 <= current_num <= 399:
        p2 = p2 + 1
    elif  399 < current_num <= 599:
        p3 = p3 + 1
    elif 599 < current_num <= 799:
        p4 = p4 + 1
    elif current_num >= 800:
        p5 = p5 + 1

percent_1= p1/numbers * 100
percent_2= p2/numbers * 100
percent_3= p3/numbers * 100
percent_4= p4/numbers * 100
percent_5= p5/numbers * 100
print(f"{percent_1:.2f}%")
print(f"{percent_2:.2f}%")
print(f"{percent_3:.2f}%")
print(f"{percent_4:.2f}%")
print(f"{percent_5:.2f}%")