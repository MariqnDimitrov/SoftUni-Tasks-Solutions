number_of_usernames = int(input())
username_set = set()
for _ in range(number_of_usernames):
    username_set.add(input())
print(*username_set, sep="\n")

