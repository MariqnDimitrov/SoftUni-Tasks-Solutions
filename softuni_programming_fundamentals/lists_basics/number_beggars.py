coins = input().split(", ")
beggars_count = int(input())
total_beggars_sum = []
integer_coins = []
beggar_coins = []
for element in coins:
    integer_coins.append(int(element))
for beggar in range(beggars_count):
    for coin in integer_coins[beggar::beggars_count]:
        beggars_sum = 0
        beggar_coins.append(coin)
    beggars_sum = sum(beggar_coins)
    total_beggars_sum.append(beggars_sum)
    beggar_coins = []
print(total_beggars_sum)