def loading_bar(some_number):
    loaded_percent = some_number // 10
    string_percent = "%" * loaded_percent
    if some_number == 100:
        return f"{some_number}% Complete!\n" \
               f"[{string_percent}]"
    left_to_load = 10 - loaded_percent
    string_dots = "." * left_to_load
    progress = string_percent + string_dots
    return f"{some_number}% [{progress}]\n" \
           f"Still loading..."
number = int(input())
print(loading_bar(number))