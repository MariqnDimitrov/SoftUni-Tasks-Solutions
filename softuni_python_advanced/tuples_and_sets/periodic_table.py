number_chemical_elements = int(input())
unique_elements_set = set()
for _ in range(number_chemical_elements):
    chemical_elements = input().split()
    for element in chemical_elements:
        unique_elements_set.add(element)
print(*unique_elements_set, sep="\n")

