number = int(input())
for i in range(number):
    for f in range(number):
        for k in range(number):
            print(f"{chr(97 + i)}{chr(97 + f)}{chr(97 + k)}")