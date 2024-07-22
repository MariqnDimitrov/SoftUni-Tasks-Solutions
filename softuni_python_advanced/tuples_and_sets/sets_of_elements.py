n, m = [int(numbers) for numbers in input().split()]
n_set = set([input() for _ in range(n)])
m_set = set([input() for _ in range(m)])
unique_elements = n_set.intersection(m_set)
print("\n".join(unique_elements))
