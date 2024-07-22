number_decorations = int(input())
days_until_christmas = int(input())
ornament_set = 2
tree_skirt = 5
tree_garland = 3
tree_lights = 15
spirit = 0
spend_money = 0
for day in range(1, days_until_christmas + 1):
    if day % 11 == 0:
        number_decorations += 2
    if day % 2 == 0:
        spend_money += ornament_set * number_decorations
        spirit += 5
    if day % 3 == 0:
        spend_money += (tree_skirt + tree_garland) * number_decorations
        spirit += 13
    if day % 5 == 0:
        spend_money += tree_lights * number_decorations
        spirit += 17
        if day % 3 == 0:
            spirit += 30
    if day % 10 == 0:
        spirit -= 20
        spend_money += (tree_skirt + tree_garland + tree_lights)
        if days_until_christmas == day:
            spirit -= 30
print(f"Total cost: {spend_money}")
print(f"Total spirit: {spirit}")