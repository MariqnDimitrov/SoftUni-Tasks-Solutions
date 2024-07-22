rows = int(input())
matrix = [[int(x) for x in input().split(" ")] for _ in range(rows)]
primary_diagonal = [matrix[i][i] for i in range(rows)]
second_diagonal = [matrix[i][- i - 1] for i in range(rows)]
print(abs(sum(primary_diagonal) - sum(second_diagonal)))