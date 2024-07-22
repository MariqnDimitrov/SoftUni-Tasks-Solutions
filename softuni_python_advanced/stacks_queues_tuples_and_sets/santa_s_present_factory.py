from collections import deque
materials = [int(x) for x in input().split()]
magic = deque(int(x) for x in input().split())
doll_count = 0
train_count = 0
teddy_bear_count = 0
bicycle_count = 0
presents_are_crafted = False
while magic and materials:
    total_magic = materials[-1] * magic[0]
    if total_magic == 150:
        doll_count += 1
        materials.pop()
        magic.popleft()
    elif total_magic == 250:
        train_count += 1
        materials.pop()
        magic.popleft()
    elif total_magic == 300:
        teddy_bear_count += 1
        materials.pop()
        magic.popleft()
    elif total_magic == 400:
        bicycle_count += 1
        materials.pop()
        magic.popleft()
    elif total_magic < 0:
        current_material = materials.pop()
        current_magic = magic.popleft()
        materials.append(current_material + current_magic)
    elif materials[-1] == 0 and magic[0] == 0:
        materials.pop()
        magic.popleft()
    elif materials[-1] == 0:
        materials.pop()
    elif magic[0] == 0:
        magic.popleft()
    else:
        magic.popleft()
        materials[-1] += 15
    if doll_count >= 1 and train_count >= 1:
        presents_are_crafted = True
    if teddy_bear_count >= 1 and bicycle_count >= 1:
        presents_are_crafted = True
if presents_are_crafted:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials:
    print("Materials left: ", end="")
    print(*reversed(materials), sep=", ")
if magic:
    print("Magic left: ", end="")
    print(*magic, sep=", ")
if bicycle_count >= 1:
    print(f"Bicycle: {bicycle_count}")
if doll_count >= 1:
    print(f"Doll: {doll_count}")
if train_count >= 1:
    print(f"Train: {train_count}")
if teddy_bear_count >= 1:
    print(f"Teddy bear: {teddy_bear_count}")








