file_directory = input().split("\\")
file_name, extension = file_directory[-1].split(".")
print(f"File name: {file_name}")
print(f"File extension: {extension}")