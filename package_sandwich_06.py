# 6번. 샌드위치 포장

def solution(data):
  sample = '12341'
  s = ''.join(map(str, data))
  count = 0

  while s.find(sample) != -1:
    s = s.replace(sample, '', 1) # sample값을 1번 바꿈
    count += 1
  return count

print(solution([1, 1, 1, 2, 3, 4, 1, 2, 3, 4, 1])) # 2
