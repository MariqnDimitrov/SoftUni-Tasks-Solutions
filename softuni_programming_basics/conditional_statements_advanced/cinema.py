projection_type = input()
number_columns = int(input())
number_rows = int(input())
final_price = 0
price = number_rows * number_columns
if projection_type == "Premiere":
    final_price= price * 12.00
elif projection_type == "Normal":
    final_price= price * 7.50
else:
    final_price= price * 5.00
print(f"{final_price:.2f} leva")