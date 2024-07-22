from collections import deque
expression = input().split()
numbers = deque()
possible_operators = "*+-/"
for char in expression:
    if char not in possible_operators:
        numbers.append(int(char))
    else:
        while len(numbers) > 1:
            first_num = numbers.popleft()
            second_num = numbers.popleft()
            if char == "+":
                numbers.appendleft(first_num + second_num)
            elif char == "-":
                numbers.appendleft(first_num - second_num)
            elif char == "/":
                numbers.appendleft(first_num // second_num)
            elif char == "*":
                numbers.appendleft(first_num * second_num)
print(numbers[0])