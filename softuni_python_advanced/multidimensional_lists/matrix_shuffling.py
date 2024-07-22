def is_coordinates_valid(row, col, r1, c1, r2, c2):
    if r1 > row or r2 > row or c1 > col or c2 > col:
        return False
    return True

matrix = []
rows, cols = [int(x) for x in input().split()]
for rows1 in range(rows):
    elements = input().split()
    matrix.append([])
    for cols1 in range(cols):
        matrix[rows1].append(elements[cols1])
while True:
    command = input().split()
    if command[0] == "END":
        break
    if len(command) == 5 and command[0] == "swap":
        row1, col1, row2, col2 = int(command[1]), int(command[2]), int(command[3]), int(command[4])
        if is_coordinates_valid(rows, cols, row1, col1, row2, col2):
            matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
            for row in range(rows):
                print(*matrix[row], sep=" ")
        else:
            print("Invalid input!")
    else:
        print("Invalid input!")



