group_budget = int(input())
season = input()
fisherman_number = int(input())
price_boat = 0
if season == "Spring":
    price_boat = 3000
elif season == "Summer":
    price_boat = 4200
elif season == "Autumn":
    price_boat = 4200
elif season == "Winter":
    price_boat = 2600
if fisherman_number <= 6:
    discount = price_boat * 0.10
    price_boat -= discount
elif 6 < fisherman_number <= 11:
    discount = price_boat * 0.15
    price_boat -= discount
elif 12 <= fisherman_number:
    discount = price_boat * 0.25
    price_boat -= discount
if fisherman_number % 2 == 0 and season != "Autumn":
    discount = price_boat * 0.05
    price_boat -= discount
needed_money=abs(group_budget - price_boat)
if group_budget >= price_boat:
    print(f"Yes! You have {needed_money:.2f} leva left.")
else:
    print(f"Not enough money! You need {needed_money:.2f} leva.")