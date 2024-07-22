wonderland_size = int(input())
wonderland = [[x for x in input().split()] for _ in range(wonderland_size)]
alice_location = []
possible_movements = {"up": (-1, 0), "right": (0, 1), "down": (1, 0), "left": (0, -1)}
tea_bags = 0
for row in range(wonderland_size):
    for col in range(wonderland_size):
        if wonderland[row][col] == "A":
            alice_location = [row, col]
            wonderland[row][col] = "*"
            break
while True:
    commands = input()
    alice_location[0] += possible_movements[commands][0]
    alice_location[1] += possible_movements[commands][1]
    if alice_location[0] >= wonderland_size or alice_location[1] >= wonderland_size:
        print("Alice didn't make it to the tea party.")
        break
    elif alice_location[0] >= wonderland_size and alice_location[1] >= wonderland_size:
        print("Alice didn't make it to the tea party.")
        break
    elif wonderland[alice_location[0]][alice_location[1]] == "R":
        wonderland[alice_location[0]][alice_location[1]] = "*"
        print("Alice didn't make it to the tea party.")
        break
    elif wonderland[alice_location[0]][alice_location[1]] == ".":
        wonderland[alice_location[0]][alice_location[1]] = "*"
        continue
    elif wonderland[alice_location[0]][alice_location[1]] == "*":
        continue
    tea_bags += int(wonderland[alice_location[0]][alice_location[1]])
    wonderland[alice_location[0]][alice_location[1]] = "*"
    if tea_bags >= 10:
        print("She did it! She went to the party.")
        break
for rows in wonderland:
    print(*rows)

