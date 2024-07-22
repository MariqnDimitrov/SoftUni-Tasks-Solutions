chicken_menu=int(input())*10.35
fish_menu=int(input())*12.40
vegetarian_menu=int(input())*8.15
menu_price=chicken_menu + fish_menu + vegetarian_menu
dessert=menu_price*0.20
final_price=menu_price + dessert + 2.50
print(final_price)