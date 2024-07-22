price_trip=float(input())
number_puzzles=int(input())
number_talking_dolls=int(input())
number_bears=int(input())
number_minions=int(input())
number_trucks=int(input())
puzzle_price=number_puzzles * 2.60
talking_dolls_price= number_talking_dolls * 3
bears_price= number_bears * 4.10
minions_price= number_minions * 8.20
trucks_price= number_trucks * 2
toys_price= trucks_price + minions_price + bears_price + talking_dolls_price + puzzle_price
number_toys= number_bears + number_trucks + number_minions + number_puzzles + number_talking_dolls
if number_toys >= 50:
    discount = toys_price * 0.25
    toys_price= toys_price - discount
rent= toys_price * 0.10
money_for_trip=toys_price - rent
left_money=abs(money_for_trip - price_trip)
if money_for_trip>= price_trip:
    print(f"Yes! {left_money:.2f} lv left.")
else:
    print(f"Not enough money! {left_money:.2f} lv needed.")