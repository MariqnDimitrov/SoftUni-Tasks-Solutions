deposit_sum = float(input())
deposit_time = int(input())
year_percentage = float(input())/100
sum1 = (deposit_sum*year_percentage) / 12
final_sum = deposit_sum + deposit_time * sum1
print(final_sum)
