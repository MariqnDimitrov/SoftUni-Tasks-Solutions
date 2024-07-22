age = int(input())
washer_price= float(input())
toy_price= int(input())
birthday_money=0
toy_count=0
final_money = 0
brothers_money=0
for i in range(1 ,age + 1):
    if i % 2 == 0:
        brothers_money = brothers_money + 1
        birthday_money = birthday_money + 10
        final_money = final_money + birthday_money

    else:
        toy_count = toy_count + 1
toy_money = toy_count * toy_price
money = final_money + toy_money - brothers_money
diff=abs(money - washer_price)
if money >= washer_price:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")