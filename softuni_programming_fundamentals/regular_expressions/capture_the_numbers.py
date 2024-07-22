import re
text = input()
list_of_matches = []
while text:
    pattern = r"(\d+)"
    matches = re.findall(pattern, text)
    for match in matches:
        list_of_matches.append(match)
    text = input()
print(" ".join(list_of_matches))