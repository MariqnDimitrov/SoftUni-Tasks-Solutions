import math
group_size = int(input())
days_of_adventure = int(input())
coins = 0
for days in range(1, days_of_adventure + 1):
    coins += 50
    if days % 10 == 0:
        group_size -= 2
    if days % 15 == 0:
        group_size += 5
    food_cost = group_size * 2
    coins -= food_cost
    if days % 3 == 0:
        party_cost = group_size * 3
        coins -= party_cost
    if days % 5 == 0:
        boss_monster_reward = group_size * 20
        coins += boss_monster_reward
        if days % 3 == 0:
            additional_party_cost = group_size * 2
            coins -= additional_party_cost
coins_per_companion = math.floor(coins / group_size)
print(f"{group_size} companions received {coins_per_companion} coins each.")