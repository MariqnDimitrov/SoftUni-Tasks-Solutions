def func_executor(*args):
    function_list = []
    for function, data in args:
        function_list.append(f"{function.__name__} - {function(*data)}")
    return "\n".join(function_list)
def sum_numbers(num1, num2):
    return num1 + num2

def multiply_numbers(num1, num2):
    return num1 * num2

print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
))
