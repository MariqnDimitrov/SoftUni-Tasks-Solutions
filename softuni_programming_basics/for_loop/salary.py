number_tabs = int(input())
salary = float(input())
for i in range(1 , number_tabs + 1):
    website_name = input()
    if website_name == "Facebook":
        salary = salary - 150
    elif website_name == "Instagram":
        salary = salary - 100
    elif website_name == "Reddit":
        salary = salary - 50
    if salary <= 0:
        break
if salary <= 0:
    print("You have lost your salary.")
else:
    print(int(salary))