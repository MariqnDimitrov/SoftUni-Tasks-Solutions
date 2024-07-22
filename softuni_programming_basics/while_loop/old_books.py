searched_book = input()
counter = 0
book = ""
while True:
    book = input()

    if book == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {counter} books.")
        break
    counter += 1
    if book == searched_book:
        counter -= 1
        print(f"You checked {counter} books and found it.")
        break