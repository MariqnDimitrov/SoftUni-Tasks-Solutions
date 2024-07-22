money_for_trip = float(input())
money = float(input())
spend_count = 0
day_count = 0
while True:
    day_count += 1
    action = input()
    action_money = float(input())
    if action == "spend":
        money -= action_money
        spend_count += 1
        if spend_count == 5:
            print("You can't save the money.")
            print(f"{day_count}")
            break
    elif action == "save":
        money += action_money
        spend_count = 0
    if money < 0:
        money = 0
    if money >= money_for_trip:
        print(f"You saved the money for {day_count} days.")
        break