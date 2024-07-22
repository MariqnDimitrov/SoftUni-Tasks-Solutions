number_bad_grades = int(input())
grade_counter = 0
bad_grade_counter = 0
grade_sum = 0
last_task = ""
while True:
    task_name = input()
    if task_name == 'Enough':
        average_grade = grade_sum / grade_counter
        print(f"Average score: {average_grade:.2f}")
        print(f"Number of problems: {grade_counter}")
        print(f"Last problem: {last_task}")
        break
    last_task = task_name
    grade = int(input())
    grade_counter += 1
    if grade <= 4:
        bad_grade_counter += 1
    if bad_grade_counter == number_bad_grades:
        print(f"You need a break, {bad_grade_counter} poor grades.")
        break
    grade_sum += grade