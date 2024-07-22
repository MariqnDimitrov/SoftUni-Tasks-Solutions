film_budget=float(input())
number_statist=int(input())
clothing_price=float(input())
decor= film_budget*0.10
if number_statist>150:
    discount= clothing_price * 0.10
    clothing_price= clothing_price - discount
final_clothing_price= clothing_price * number_statist
final_price=final_clothing_price + decor
left_money=abs(film_budget - final_price)
if final_price > film_budget:
    print("Not enough money!")
    print(f"Wingard needs {left_money:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {left_money:.2f} leva left.")