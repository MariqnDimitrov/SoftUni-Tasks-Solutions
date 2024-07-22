import sys
numbers = int(input())
biggest = -sys.maxsize
total_sum = 0
for i in range(1,numbers + 1):
    current_num = int(input())
    total_sum = total_sum + current_num
    if current_num > biggest:
        biggest = current_num
final_sum = total_sum - biggest
diff = abs(final_sum - biggest)
if final_sum == biggest:
    print("Yes")
    print(f"Sum = {biggest}")
else:
    print("No")
    print(f"Diff = {diff}")