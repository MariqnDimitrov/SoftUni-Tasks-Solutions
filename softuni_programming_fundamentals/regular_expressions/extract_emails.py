import re
text = input()
pattern = r"\s(([a-z0-9]+[a-z0-9\.\-\_]+)@([a-z\-]+)(\.[a-z]+)+)\b"
matches = re.findall(pattern, text)
for match in matches:
    print(match[0])