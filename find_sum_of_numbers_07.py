# 순열 조합
import itertools

array = ['A', 'B', 'C']
permutation = itertools.permutations(array, 2) # 순서가 고려됨 (순열)
combine = itertools.combinations(array, 2) # 순서가 고려되지 않음 (조합)

print(list(permutation)) # [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
print(list(combine)) # [('A', 'B'), ('A', 'C'), ('B', 'C')]