capacity = 255
pour_number = int(input())
poured_liters = 0
for number in range(pour_number):
    liters = int(input())
    if poured_liters + liters > capacity:
        print("Insufficient capacity!")
        continue
    else:
        poured_liters += liters
print(poured_liters)