rows, cols = [int(x) for x in input().split()]
start_value = 97
matrix = []
for row in range(rows):
    matrix.append([])
    for col in range(cols):
        matrix[row].append(chr(start_value + row) + chr(start_value + col + row) + chr(start_value + row))
for i in range(rows):
    print(*matrix[i], sep=" ")


