import math
tournament_numbers = int(input())
starting_points = int(input())
final_points = 0
won=0
for i in range(1, tournament_numbers + 1):
    stage = input()
    if stage == "W":
        final_points = final_points + 2000
        won = won + 1
    elif stage == "F":
        final_points = final_points + 1200
    elif stage == "SF":
        final_points = final_points + 720
percent_won_tournaments = (won / tournament_numbers) * 100
average_points = math.floor(final_points / tournament_numbers)
final_points = final_points + starting_points
print(f"Final points: {final_points}")
print(f"Average points: {average_points}")
print(f"{percent_won_tournaments:.2f}%")