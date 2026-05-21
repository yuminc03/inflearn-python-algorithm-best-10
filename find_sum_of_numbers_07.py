# 7번. 두 수의 합 찾기 (투포인터, 슬라이딩 윈도우)
# 순열 조합
import itertools

# 순열과 조합에 대한 이해
array = ['A', 'B', 'C']
permutation = itertools.permutations(array, 2) # 순서가 고려됨 (순열)
combine = itertools.combinations(array, 2) # 순서가 고려되지 않음 (조합)
# print(list(permutation)) # [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
# print(list(combine)) # [('A', 'B'), ('A', 'C'), ('B', 'C')]

# 알고리즘 문제 풀기

def solution(data):
  combine = list(itertools.combinations(data[0], 2))
  result = list(filter(lambda x: sum(x) == data[1], combine))[0]
  firstIndex = data[0].index(result[0])
  secondIndex = data[0].index(result[1], firstIndex + 1)
  return sorted([firstIndex, secondIndex])

print(solution([[4, 9, 11, 2], 6]))

