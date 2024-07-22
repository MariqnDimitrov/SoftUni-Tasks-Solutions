number_pens=int(input())
number_markers=int(input())
liters_preparat=int(input())
discount_percentage=int(input())/100
pen_price=number_pens*5.80
marker_price=number_markers*7.20
preparat_price=liters_preparat*1.20
product_price=preparat_price + marker_price + pen_price
final_price=product_price - (product_price*discount_percentage)
print(final_price)