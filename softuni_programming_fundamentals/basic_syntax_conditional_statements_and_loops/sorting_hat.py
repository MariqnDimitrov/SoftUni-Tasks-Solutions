Voldemort = False
while True:
    student_name = input()
    if student_name == "Welcome!":
        break
    if student_name == "Voldemort":
        Voldemort = True
        print("You must not speak of that name!")
        break
    if len(student_name) < 5:
        print(f"{student_name} goes to Gryffindor.")
    elif len(student_name) == 5:
        print(f"{student_name} goes to Slytherin.")
    elif len(student_name) == 6:
        print(f"{student_name} goes to Ravenclaw.")
    else:
        print(f"{student_name} goes to Hufflepuff.")
if Voldemort == False:
    print("Welcome to Hogwarts.")