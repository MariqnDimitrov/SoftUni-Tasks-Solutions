registered_numbers = {}
number_of_commands = int(input())
for commands in range(number_of_commands):
    command = input().split()
    username = command[1]
    if command[0] == "register":
        license_plate_number = command[2]
        if username not in registered_numbers:
            registered_numbers[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate_number}")
    if command[0] == "unregister":
        if username not in registered_numbers:
            print(f"ERROR: user {username} not found")
        else:
            registered_numbers.pop(username)
            print(f"{username} unregistered successfully")

for key, value in registered_numbers.items():
    print(f"{key} => {value}")