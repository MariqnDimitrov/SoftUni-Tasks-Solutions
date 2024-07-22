import os
command = input().split("-")
while command[0] != "End":
    command_name = command[0]
    file_name = command[1]
    if command_name == "Create":
        open(file_name, "w").close()
    elif command_name == "Add":
        text = command[2]
        with open(file_name, "a") as f:
            f.write(f"{text}\n")
    elif command_name == "Replace":
        old_string = command[2]
        new_string = command[3]
        if os.path.exists(file_name):
            with open(file_name, 'r') as f:
                content = f.read()
            with open(file_name, "w") as f:
                f.write(content.replace(old_string, new_string))
        else:
            print("An error occurred")
    elif command_name == "Delete":
        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            print("An error occurred")
    command = input().split("-")

