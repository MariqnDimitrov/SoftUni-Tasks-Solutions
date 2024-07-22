import re
text = input()
pattern = r"\b_([A-Za-z]+)\b"
matches = re.findall(pattern, text)
print(",".join(matches))