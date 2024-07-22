students_info = {}
number_of_students = int(input())
for student in range(number_of_students):
    name = input()
    grade = float(input())
    if name not in students_info.keys():
        students_info[name] = []
    students_info[name].append(grade)
for key, value in students_info.items():
    average_grade = sum(value) / len(value)
    if average_grade >= 4.50:
        print(f"{key} -> {average_grade:.2f}")