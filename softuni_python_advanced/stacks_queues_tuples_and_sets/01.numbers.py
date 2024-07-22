first_set = set(int(x) for x in input().split())
second_set = set(int(x) for x in input().split())
number_of_commands = int(input())
for number in range(number_of_commands):
    command = input().split()
    if command[0] == "Add":
        if command[1] == "First":
            for num1 in command[2:]:
                first_set.add(int(num1))
        elif command[1] == "Second":
            for num2 in command[2:]:
                second_set.add(int(num2))
    elif command[0] == "Remove":
        if command[1] == "First":
            for removed_num1 in command[2:]:
                if int(removed_num1) in first_set:
                    first_set.remove(int(removed_num1))
        elif command[1] == "Second":
            for removed_num2 in command[2:]:
                if int(removed_num2) in second_set:
                    second_set.remove(int(removed_num2))
    else:
        print(first_set.issubset(second_set) or second_set.issubset(first_set))
print(*sorted(first_set), sep=", ")
print(*sorted(second_set), sep=", ")






