group_number = int(input())
musala_group=0
monbland_group=0
kilimanjaro_group=0
k2_group=0
everest_group=0
final_people_number = 0
for i in range(group_number):
    number_people = int(input())
    final_people_number = final_people_number + number_people
    if number_people <= 5:
        musala_group = musala_group + number_people
    elif 6 <= number_people <= 12:
        monbland_group = monbland_group + number_people
    elif 13 <= number_people <= 25:
        kilimanjaro_group = kilimanjaro_group + number_people
    elif 26 <= number_people <= 40:
        k2_group = k2_group + number_people
    elif number_people >= 41:
        everest_group = everest_group + number_people
musala_percent = (musala_group / final_people_number) * 100
monbland_percent = (monbland_group / final_people_number) * 100
kilimanjaro_percent = (kilimanjaro_group / final_people_number) * 100
k2_percent = (k2_group / final_people_number) * 100
everest_percent = (everest_group / final_people_number) * 100
print(f"{musala_percent:.2f}%")
print(f"{monbland_percent:.2f}%")
print(f"{kilimanjaro_percent:.2f}%")
print(f"{k2_percent:.2f}%")
print(f"{everest_percent:.2f}%")