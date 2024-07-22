free_space_width = int(input())
free_space_len = int(input())
free_space_high = int(input())
total_free_space = free_space_high * free_space_len * free_space_width
needed_space = 0
while True:
    boxes = input()
    if boxes == "Done":
        if diff >= 0:
            print(f"{diff} Cubic meters left.")
            break
    boxes = int(boxes)
    needed_space += boxes
    diff = abs(total_free_space - needed_space)
    if total_free_space < needed_space:
        print(f"No more free space! You need {diff} Cubic meters more.")
        break