steps_count = 0
diff = 0
while True:
    steps = input()
    if steps == "Going home":
        steps_to_home = int(input())
        steps_count += steps_to_home
        diff = abs(steps_count - 10000)
        if steps_count < 10000:
            print(f"{diff} more steps to reach goal.")
            break
        else:
            diff = abs(steps_count - 10000)
            print("Goal reached! Good job!")
            print(f"{diff} steps over the goal!")
            break

    steps = int(steps)
    steps_count += steps
    if steps_count >= 10000:
        diff = abs(steps_count - 10000)
        print("Goal reached! Good job!")
        print(f"{diff} steps over the goal!")
        break