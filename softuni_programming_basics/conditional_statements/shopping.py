budget=float(input())
number_video=int(input())
number_processors=int(input())
number_ram=int(input())
price_video= number_video*250
price_processor= price_video * 0.35 * number_processors
price_ram= price_video * 0.10 * number_ram
final_price=price_ram + price_processor + price_video
if number_video > number_processors:
    discount= final_price * 0.15
    final_price= final_price - discount
left_money=abs(final_price - budget)
if budget >= final_price:
    print(f"You have {left_money:.2f} leva left!")
else:
    print(f"Not enough money! You need {left_money:.2f} leva more!")