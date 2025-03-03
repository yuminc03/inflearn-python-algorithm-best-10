# 4번. 꿈의 설계(정규표현식)

import re

def solution(data):
  훈련수치 = {}
  고민수치 = {}
  원래미래 = 0
  바뀐미래 = 0

  # 훈련수치
  for i in data[0].split('.')[:-1]:
    key = re.findall(r'[a-zA-Z]', i)[0]
    value = re.findall(r'\d+', i)[0]
    if key in 훈련수치:
      훈련수치[key] += int(value)
    else:
      훈련수치[key] = int(value)

  # 고민수치
  for i in data[1].split('.')[:-1]:
    key = re.findall(r'[a-zA-Z]', i)[0]
    value = re.findall(r'\d+', i)[0]
    if key in 고민수치:
      고민수치[key] += int(value)
    else:
      고민수치[key] = int(value)

  # 원래미래
  for i in 훈련수치.keys():
    if i in 고민수치:
      원래미래 += 훈련수치[i] * 고민수치[i]

  if 원래미래 == 0:
    return '미래가 보이지 않습니다.'

  # 가장 큰 값에 100을 더함
  훈련수치중가장큰값 = max(훈련수치.values())
  고민수치중가장큰값 = max(고민수치.values())
  for i in 훈련수치:
    if 훈련수치[i] == 훈련수치중가장큰값:
      훈련수치[i] += 100

  for i in 고민수치:
    if 고민수치[i] == 고민수치중가장큰값:
      고민수치[i] += 100

  for i in 훈련수치.keys():
    if i in 고민수치:
      바뀐미래 += 훈련수치[i] * 고민수치[i]

  return f'최종 꿈의 설계는 원래 미래 {원래미래}, 바뀐 미래 {바뀐미래}입니다. 이 수치대로 Vision을 만듭니다.'

# 최종 꿈의 설계는 원래 미래 260,바뀐 미래 14760입니다. 이 수치대로 Vision을 만듭니다.
print(solution(['10 - A. 20 - B. 30 - A.', '1 - A. 1 - A. 1 - A. 1 - A. 2 - B. 1 - A. 1 - B.']))