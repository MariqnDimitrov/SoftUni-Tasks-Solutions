flower_type = input()
number_flowers = int(input())
budget = int(input())
price=0
if flower_type == "Roses":
    price = number_flowers * 5
    if number_flowers > 80:
        discount = price * 0.10
        price = price - discount
elif flower_type == "Dahlias":
    price = number_flowers * 3.80
    if number_flowers > 90:
        discount = price * 0.15
        price = price - discount
elif flower_type == "Tulips":
    price = number_flowers * 2.80
    if number_flowers > 80:
        discount = price * 0.15
        price = price - discount
elif flower_type == "Narcissus":
    price = number_flowers * 3
    if number_flowers < 120:
        price = price * 1.15
elif flower_type == "Gladiolus":
    price = number_flowers * 2.50
    if number_flowers < 80:
        price = price * 1.20
needed_money = abs(budget - price)
if budget >= price:
    print(f"Hey, you have a great garden with {number_flowers} {flower_type} and {needed_money:.2f} leva left.")
else:
    print(f"Not enough money, you need {needed_money:.2f} leva more.")