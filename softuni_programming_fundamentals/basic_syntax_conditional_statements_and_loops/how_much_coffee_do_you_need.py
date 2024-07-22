coffee = 0
while True:
    activity = input()
    if activity == "END":
        break
    if activity == "cat" or activity == "dog":
        coffee += 1
    elif activity == "CAT" or activity == "DOG":
        coffee += 2
    elif activity == "coding":
        coffee += 1
    elif activity == "CODING":
        coffee += 2
    elif activity == "movie":
        coffee += 1
    elif activity == "MOVIE":
        coffee += 2
if coffee > 5:
    print("You need extra sleep")
else:
    print(coffee)