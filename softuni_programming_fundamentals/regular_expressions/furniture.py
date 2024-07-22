import re
command = input()
furniture = []
total_price = 0
pattern = r">>([A-Za-z]+)<<([0-9\.]+)!([0-9]+)\b"
while command != "Purchase":
    valid_command = re.findall(pattern, command)
    for item in valid_command:
        furniture.append(item[0])
        single_price = float(item[1])
        quantity = float(item[2])
        total_price += single_price * quantity
    command = input()
print("Bought furniture:")
for items in furniture:
    print(items)
print(f"Total money spend: {total_price:.2f}")