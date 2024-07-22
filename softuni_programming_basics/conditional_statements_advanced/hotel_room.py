month = input()
number_overnights = int(input())
apartment_price = 0
studio_price = 0
if month == "May" or month == "October":
    apartment_price = 65 * number_overnights
    studio_price = 50 * number_overnights
    if number_overnights > 14:
        studio_discount = studio_price * 0.3
        studio_price -= studio_discount
        apartment_discount = apartment_price * 0.1
        apartment_price -= apartment_discount
    elif number_overnights > 7:
        studio_discount = studio_price * 0.05
        studio_price -= studio_discount
if month == "June" or month == "September":
    apartment_price = 68.70 * number_overnights
    studio_price = 75.20 * number_overnights
    if number_overnights > 14:
        studio_discount = studio_price * 0.2
        studio_price -= studio_discount
        apartment_discount = apartment_price * 0.1
        apartment_price -= apartment_discount
if month == "July" or month == "August":
    apartment_price = 77 * number_overnights
    studio_price = 76 * number_overnights
    if number_overnights > 14:
        apartment_discount = apartment_price * 0.1
        apartment_price -= apartment_discount
print(f"Apartment: {apartment_price:.2f} lv.")
print(f"Studio: {studio_price:.2f} lv.")