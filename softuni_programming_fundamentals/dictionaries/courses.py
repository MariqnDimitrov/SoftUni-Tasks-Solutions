courses_dict = {}
student_info = input()
while student_info != "end":
    course_name, student_name = student_info.split(" :")
    if course_name not in courses_dict:
        courses_dict[course_name] = []
    courses_dict[course_name].append(student_name)
    student_info = input()
for key, value in courses_dict.items():
    print(f"{key}: {len(value)}")
    for students in range(len(value)):
        print(f"--{value[students]}")