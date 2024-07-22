country_names = input().split(", ")
country_capitals = input().split(", ")
for country in range(len(country_capitals)):
    country_dict = {country_names[index]: country_capitals[index]for index in range(len(country_capitals))}
for key, item in country_dict.items():
    print(f"{key} -> {item}")