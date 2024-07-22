eggs = 1
flour = 1
milk = 0.25
loaf = 0
colored_eggs = 0
budget = float(input())
flour_price = float(input())
egg_price = flour_price * 0.75
milk_price = (flour_price * 1.25)/4
total_price = milk_price + egg_price + flour_price
while budget >= total_price:
    budget -= flour_price + egg_price + milk_price
    loaf += 1
    colored_eggs += 3
    if loaf % 3 == 0:
        colored_eggs -= loaf - 2
print(f"You made {loaf} loaves of Easter bread! Now you have {colored_eggs}"
      f" eggs and {budget:.2f}BGN left.")