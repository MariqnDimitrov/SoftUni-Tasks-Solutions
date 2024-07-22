field_size = int(input())
field = [[x for x in input().split()] for _ in range(field_size)]
starting_bunny_position = []
most_eggs_bunny_path = []
max_sum = float("-inf")
max_direction = ""
possible_moves = [[1, 0, "down"], [-1, 0, "up"], [0, 1, "right"], [0, -1, "left"]]
for row in range(field_size):
    for col in range(field_size):
        if field[row][col] == "B":
            starting_bunny_position = [row, col]
for move in possible_moves:
    current_bunny_position = [starting_bunny_position[0], starting_bunny_position[1]]
    current_sum = 0
    current_bunny_path = []
    for i in range(field_size):
        current_bunny_position[0] += move[0]
        current_bunny_position[1] += move[1]
        if current_bunny_position[0] >= field_size or current_bunny_position[1] >= field_size:
            break
        elif current_bunny_position[0] < 0 or current_bunny_position[-1] < 0:
            break
        elif field[current_bunny_position[0]][current_bunny_position[1]] == "X":
            break
        current_sum += int(field[current_bunny_position[0]][current_bunny_position[1]])
        current_bunny_path.append([current_bunny_position[0], current_bunny_position[1]])
    if current_sum > max_sum:
        max_sum = current_sum
        most_eggs_bunny_path = current_bunny_path
        max_direction = move[2]
print(max_direction)
[print(row) for row in most_eggs_bunny_path]
print(max_sum)




