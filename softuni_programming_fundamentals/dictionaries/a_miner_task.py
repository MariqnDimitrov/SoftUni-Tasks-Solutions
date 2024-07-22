resources_dictionary = {}
while True:
    resources = input()
    if resources == "stop":
        break
    quantity = int(input())
    if resources not in resources_dictionary:
        resources_dictionary[resources] = 0
    resources_dictionary[resources] += quantity
for key, item in resources_dictionary.items():
    print(f"{key} -> {item}")