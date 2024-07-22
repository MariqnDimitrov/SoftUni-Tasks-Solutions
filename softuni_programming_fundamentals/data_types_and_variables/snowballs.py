number_of_snowballs = int(input())
highest_value = 0
highest_weight = 0
lowest_time_needed = 0
highest_quality = 0
for snowball in range(number_of_snowballs):
    weight = int(input())
    time_needed = int(input())
    quality = int(input())
    value = (weight / time_needed) ** quality
    if value > highest_value:
        highest_value = int(value)
        highest_weight = weight
        lowest_time_needed = time_needed
        highest_quality = quality
print(f"{highest_weight} : {lowest_time_needed} = {highest_value} ({highest_quality})")