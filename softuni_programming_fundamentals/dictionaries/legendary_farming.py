items = {"shards": 0, "fragments": 0, "motes": 0}
obtained = False
while not obtained:
    materials = input().split()
    for index in range(0, len(materials), 2):
        value = int(materials[index])
        key = materials[index + 1].lower()
        if key not in items.keys():
            items[key] = 0
        items[key] += value
        if items["shards"] >= 250:
            items["shards"] -= 250
            print("Shadowmourne obtained!")
            obtained = True
        elif items["fragments"] >= 250:
            items["fragments"] -= 250
            print("Valanyr obtained!")
            obtained = True
        elif items["motes"] >= 250:
            items["motes"] -= 250
            print("Dragonwrath obtained!")
            obtained = True
            if obtained:
                break
        if obtained:
            break
for material, quantity in items.items():
    print(f"{material}: {quantity}")