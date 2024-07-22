import sys
rows, cols = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(rows)]
max_matrix = []
max_sum = -sys.maxsize
current_matrix = []
matrix_row = []
for row in range(rows - 2):
    for col in range(cols - 2):
        current_sum = 0
        for r in range(row,  row + 3):
            for c in range(col, col + 3):
                matrix_row.append(matrix[r][c])
                current_sum += matrix[r][c]
            current_matrix.append(matrix_row)
            matrix_row = []

        if current_sum > max_sum:
            max_sum = current_sum
            max_matrix = current_matrix

        current_matrix = []
print(f"Sum = {max_sum}")
for i in range(3):
    print(*max_matrix[i], sep=" ")





