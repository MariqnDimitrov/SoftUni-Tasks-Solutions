product_dict = {}
product = input().split()
while product[0] != "buy":
    name, price, quantity = product[0], float(product[1]), int(product[2])
    if name not in product_dict.keys():
        product_dict[name] = [price, quantity]
    else:
        product_dict[name][1] += quantity
        product_dict[name][0] = price
    product = input().split()
for key, value in product_dict.items():
    total_price = value[0] * value[1]
    print(f"{key} -> {total_price:.2f}")