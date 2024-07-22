number_of_orders = int(input())
total_price = 0
for orders in range(1, number_of_orders + 1):
    capsule_price = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if capsule_price < 0.01:
        continue
    elif capsule_price > 100.00:
        continue
    if days < 1:
        continue
    elif days > 31:
        continue
    if capsules_per_day < 1:
        continue
    elif capsules_per_day > 2000:
        continue
    order_price = capsule_price * capsules_per_day * days
    total_price += order_price
    print(f"The price for the coffee is: ${order_price:.2f}")
print(f"Total: ${total_price:.2f}")