days = int(input())
room = input()
rating = input()
price = 0
if days < 10:
    if room == "room for one person":
        price = (days - 1) * 18.00
    elif room == "apartment":
        price = (days - 1) * 25.00
        discount = price * 0.3
        price -= discount
    elif room == "president apartment":
        price =  (days - 1) * 35.00
        discount = price * 0.1
        price -= discount
elif 10 <= days <= 15:
    if room == "room for one person":
        price = (days - 1) * 18.00
    elif room == "apartment":
        price = (days - 1) * 25.00
        discount = price * 0.35
        price -= discount
    elif room == "president apartment":
        price = (days - 1) * 35.00
        discount = price * 0.15
        price -= discount
elif days > 15:
    if room == "room for one person":
        price = (days - 1) * 18.00
    elif room == "apartment":
        price = (days - 1) * 25.00
        discount = price * 0.5
        price -= discount
    elif room == "president apartment":
        price = (days - 1) * 35.00
        discount = price * 0.2
        price -= discount
if rating == "positive":
    price = price * 1.25
else:
    price = price * 0.9
print(f"{price:.2f}")