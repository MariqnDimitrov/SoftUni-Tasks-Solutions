from collections import deque
working_bees = deque(int(x) for x in input().split())
nectar = [int(x) for x in input().split()]
symbols = deque(input().split())
honey = 0
while nectar and working_bees:
    if working_bees[0] <= nectar[-1]:
        if symbols[0] == "+":
            current_honey = working_bees[0] + nectar[-1]
            honey += abs(current_honey)
        elif symbols[0] == "-":
            current_honey = working_bees[0] - nectar[-1]
            honey += abs(current_honey)
        elif symbols[0] == "*":
            current_honey = working_bees[0] * nectar[-1]
            honey += abs(current_honey)
        elif symbols[0] == "/":
            if nectar[-1] == 0:
                working_bees.popleft()
                nectar.pop()
                symbols.popleft()
                continue
            current_honey = working_bees[0] / nectar[-1]
            honey += abs(current_honey)
        working_bees.popleft()
        nectar.pop()
        symbols.popleft()
    else:
        nectar.pop()
        continue
print(f"Total honey made: {honey}")
if nectar:
    print("Nectar left: ", end="")
    print(*nectar, sep=", ")
if working_bees:
    print("Bees left: ", end="")
    print(*working_bees, sep=", ")








