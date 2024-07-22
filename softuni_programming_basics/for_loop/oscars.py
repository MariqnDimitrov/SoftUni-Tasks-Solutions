actor_name = input()
academy_points = float(input())
number_testers = int(input())
final_points = academy_points
for i in range(1 , number_testers + 1 ):
    tester_name = input()
    tester_points = float(input())
    final_tester_points= (len(tester_name) * tester_points)/2
    final_points = final_points + final_tester_points
    if final_points >= 1250.5:
        break
diff = abs(final_points - 1250.5)
if final_points >= 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {final_points:.1f}!")
else:
    print(f"Sorry, {actor_name} you need {diff:.1f} more!")