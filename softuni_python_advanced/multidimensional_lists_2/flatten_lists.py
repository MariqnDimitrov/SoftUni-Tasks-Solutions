matrix = [[int(number) for number in x.split(" ") if not number == ""] for x in input().split("|")]
final_list = []
for numbers in range(len(matrix) - 1, -1, -1):
    for element in  matrix[numbers]:
        final_list.append(element)
print(*final_list)

