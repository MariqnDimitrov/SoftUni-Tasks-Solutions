def age_assignment(*args,**kwargs):
    personal_info_dict = {}
    final_list = []
    for names in args:
        if names[0] in kwargs.keys():
            personal_info_dict[names] = kwargs[names[0]]
    personal_info_dict = dict(sorted(personal_info_dict.items(), key=lambda x: x[0]))
    for name, age in personal_info_dict.items():
        final_list.append(f"{name} is {age} years old.")
    return "\n".join(final_list)

print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))


