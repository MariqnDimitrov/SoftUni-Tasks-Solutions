phone_number_dict = {}
while True:
    contact = input()
    if "-" not in contact:
        break
    name, number = contact.split("-")
    phone_number_dict[name] = number
for search in range(int(contact)):
    searched_name = input()
    if searched_name in phone_number_dict.keys():
        print(f"{searched_name} -> {phone_number_dict[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")