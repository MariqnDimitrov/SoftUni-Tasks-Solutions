from collections import deque
parenthesis = deque(input())
opening_parenthesis = "([{"
closing_parenthesis = ")]}"
while parenthesis and len(parenthesis) > 1:
    if parenthesis[0] in closing_parenthesis:
        break
    index = opening_parenthesis.index(parenthesis[0])
    if parenthesis[1] == closing_parenthesis[index]:
        parenthesis.popleft()
        parenthesis.popleft()
    elif parenthesis[-1] == closing_parenthesis[index]:
        parenthesis.popleft()
        parenthesis.pop()
    else:
        break
if parenthesis:
    print("NO")
else:
    print("YES")