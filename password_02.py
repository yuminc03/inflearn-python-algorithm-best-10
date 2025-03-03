# 02. 암호문

import re

def solution(data):
  result = 0
  data = re.findall('([rev])(10|[1-9])', data)
  for i, j in data:
    result += int(j)
  result = str(result)

  return f'{result[0]}월 {result[1]}일'

print(solution('a10b9r1ce33uab8wc918v2cv11v9')) # 1월 6일
