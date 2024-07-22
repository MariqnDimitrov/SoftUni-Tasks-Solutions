number_of_names = int(input())
odd_set = set()
even_set = set()
for number in range(1, number_of_names + 1):
    name_set = sum([ord(char) for char in input()]) // number
    if name_set % 2 == 0:
        even_set.add(name_set)
    else:
        odd_set.add(name_set)
even_sum = sum(even_set)
odd_sum = sum(odd_set)
if even_sum == odd_sum:
    union_set = even_set.union(odd_set)
    print(*union_set, sep=", ")
elif even_sum < odd_sum:
    different_set = odd_set.difference(even_set)
    print(*different_set, sep=", ")
else:
    symmetric_diff_set = even_set.symmetric_difference(odd_set)
    print(*symmetric_diff_set, sep=", ")



