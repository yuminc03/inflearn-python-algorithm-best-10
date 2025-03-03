# 3번. 출정인원 선발 (정렬)

data = [
    ['A', 25, 25, 25, 25],
    ['B', 10, 12, 13, 11],
    ['C', 24, 22, 23, 21],
    ['D', 13, 22, 16, 14],
    ['E', 25, 25, 25, 25]
]

def solution(data):
  전체인원수 = len(data)
  선발해야하는인원 = int((전체인원수 * 3) / 10)
  if 선발해야하는인원 == 0:
    return

  선발된인원 = 0
  점수딕셔너리 = {}
  선발인원리스트 = []
  for i in data:
    합 = sum(i[1:])
    if 합 in 점수딕셔너리:
      점수딕셔너리[합] = 점수딕셔너리[합] + [i[0]]
    else:
      점수딕셔너리[합] = [i[0]]

  for i in sorted(list(점수딕셔너리.items()), reverse=True):
    if 선발된인원 < 선발해야하는인원 and len(i[1]) <= 선발해야하는인원:
      선발인원리스트.extend(i[1])
      선발된인원 += len(i[1])
    elif len(i[1]) > 선발해야하는인원:
      return 선발인원리스트

  return sorted(선발인원리스트, reverse=True)

solution(data)