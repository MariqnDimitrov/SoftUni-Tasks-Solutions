clothes_stack = [int(x) for x in input().split()]
rack_capacity = int(input())
rack_counter = 0
rack_clothes = []
while clothes_stack:
    if rack_capacity >= sum(rack_clothes) + clothes_stack[-1]:
        rack_clothes.append(clothes_stack.pop())
        if len(clothes_stack) == 1:
            rack_counter += 1
    else:
        rack_counter += 1
        rack_clothes = []
print(rack_counter)