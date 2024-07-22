budget = float(input())
season = input()
destination = ""
resting_place = ""
price = 0
if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        resting_place = "Camp"
        price = budget * 0.3
    elif season == "winter":
        resting_place = "Hotel"
        price = budget * 0.7
if 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        resting_place = "Camp"
        price = budget * 0.4
    elif season == "winter":
        resting_place = "Hotel"
        price = budget * 0.8
if budget > 1000:
    destination = "Europe"
    price = budget * 0.9
    resting_place = "Hotel"
print(f"Somewhere in {destination}")
print(f"{resting_place} - {price:.2f}")