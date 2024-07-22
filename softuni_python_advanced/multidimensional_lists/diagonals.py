rows = int(input())
matrix = [[int(x) for x in input().split(", ")] for _ in range(rows)]
primary_diagonal = [matrix[i][i] for i in range(rows)]
second_diagonal = [matrix[i][- i - 1] for i in range(rows)]
print(f"Primary diagonal: {', '.join([str(x) for x in primary_diagonal])}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join([str(x) for x in second_diagonal])}. Sum: {sum(second_diagonal)}")








