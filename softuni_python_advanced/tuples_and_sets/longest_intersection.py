number_intersections = int(input())
longest_intersection = set()
for number in range(number_intersections):
    first_range, second_range = input().split("-")
    first_start, first_end = first_range.split(",")
    second_start, second_end = second_range.split(",")
    first_set = set([first_numbers for first_numbers in range(int(first_start), int(first_end) + 1)])
    second_set = set([second_numbers for second_numbers in range(int(second_start), int(second_end) + 1)])
    intersection = first_set.intersection(second_set)
    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection
print(f"Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}")



