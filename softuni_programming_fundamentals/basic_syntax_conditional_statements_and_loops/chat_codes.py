number_of_messages = int(input())
for messages in range(number_of_messages):
    secret_number = int(input())
    if secret_number == 88:
        print("Hello")
    elif secret_number == 86:
        print("How are you?")
    elif secret_number < 88:
        print("GREAT!")
    else:
        print("Bye.")