import re
web_links = input()
pattern = r"(www.([A-Za-z0-9/-]+)(\.[a-z]+)+)\b"
while web_links:
    valid_web_links = re.findall(pattern, web_links)
    for link in valid_web_links:
        print(link[0])
    web_links = input()