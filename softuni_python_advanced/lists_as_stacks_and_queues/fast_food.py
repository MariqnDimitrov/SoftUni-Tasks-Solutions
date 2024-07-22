from collections import deque
food_quantity = int(input())
orders = deque([int(quantity) for quantity in input().split()])
print(max(orders))
for current_order in range(len(orders)):
    if food_quantity >= orders[0]:
        food_quantity -= orders.popleft()
    else:
        break

if orders:
    print("Orders left:", end=" ")
    while orders:
        print(orders.popleft(), end=" ")
else:
    print("Orders complete")