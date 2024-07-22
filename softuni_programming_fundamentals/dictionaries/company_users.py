company_dict = {}
company_info = input()
while company_info != "End":
    company_name, employee_id = company_info.split("->")
    if company_name not in company_dict:
        company_dict[company_name] = []
    if employee_id not in company_dict[company_name]:
        company_dict[company_name].append(employee_id)
    company_info = input()
for key, value in company_dict.items():
    print(key)
    for employee in range(len(value)):
        print(f"--{value[employee]}")