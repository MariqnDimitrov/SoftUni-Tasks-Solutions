from collections import deque
colors_substrings = deque(input().split())
main_colors = ["yellow", "red", "blue"]
secondary_colors = ["green", "purple", "orange"]
colors = []
while colors_substrings:
    if len(colors_substrings) == 1:
        if colors_substrings[0] in main_colors:
            colors.append(colors_substrings.pop())
            break
    substring_check = colors_substrings[0] + colors_substrings[-1]
    second_substring_check = colors_substrings[-1] + colors_substrings[0]
    if substring_check in main_colors:
        colors_substrings.popleft()
        colors_substrings.pop()
        colors.append(substring_check)
    elif substring_check in secondary_colors:
        if substring_check == "green":
            if "yellow" in colors_substrings and "green" in colors_substrings:
                colors_substrings.popleft()
                colors_substrings.pop()
                colors.append(substring_check)
            if substring_check == "purple":
                if "red" in colors_substrings and "blue" in colors_substrings:
                    colors_substrings.popleft()
                    colors_substrings.pop()
                    colors.append(substring_check)
            if substring_check == "orange":
                if "yellow" in colors_substrings and "red" in colors_substrings:
                    colors_substrings.popleft()
                    colors_substrings.pop()
                    colors.append(substring_check)

    else:
        if len(colors_substrings) % 2 != 0:
            colors_substrings[-1] = colors_substrings[-1][:-1]
            colors_substrings.insert((len(colors_substrings) // 2) + 1, colors_substrings[-1])
            colors_substrings[0] = colors_substrings[0][:-1]
            colors_substrings.insert((len(colors_substrings) // 2) + 1, colors_substrings[0])
        else:
            colors_substrings[-1] = colors_substrings[-1][:-1]
            colors_substrings.insert(len(colors_substrings) // 2, colors_substrings.pop())
            colors_substrings[0] = colors_substrings[0][:-1]
            colors_substrings.insert(len(colors_substrings) // 2, colors_substrings.popleft())
            if "" in colors_substrings:
                index = colors_substrings.index("")
                colors_substrings.remove(colors_substrings[index])
print(colors)



