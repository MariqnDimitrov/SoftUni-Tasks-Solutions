from collections import deque

chocolates = deque(int(x) for x in input().split(","))
cups_of_milk = deque(int(x) for x in input().split(","))
milkshakes_count = 0
while milkshakes_count < 5 and chocolates and cups_of_milk:
    if chocolates[-1] <= 0 and cups_of_milk[0] <= 0:
        chocolates.pop()
        cups_of_milk.popleft()
        continue
    if chocolates[-1] <= 0:
        chocolates.pop()
        continue
    if cups_of_milk[0] <= 0:
        cups_of_milk.popleft()
        continue
    if cups_of_milk and chocolates and milkshakes_count < 5:
        if chocolates[-1] == cups_of_milk[0]:
            milkshakes_count += 1
            chocolates.pop()
            cups_of_milk.popleft()
        else:
            cups_of_milk.rotate(-1)
            chocolates[-1] -= 5
if milkshakes_count == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print("Chocolate: ", end="")
    print(*chocolates, sep=", ")
else:
    print("Chocolate: empty")

if cups_of_milk:
    print("Milk: ", end="")
    print(*cups_of_milk, sep=", ")
else:
    print("Milk: empty")


