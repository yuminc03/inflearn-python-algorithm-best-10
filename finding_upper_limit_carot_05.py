#  5번. 상한 당근 찾기

def solution(data):
  for i in range(len(data)):
    for j in range(len(data[0])):
      if data[i][j] == '#':
          # 상
          if i != 0:
            if data[i-1][j] != '#':
              data[i-1][j] += 1

          # 하
          if i != len(data)-1: # 가장 끝에 있는지 확인
            if data[i+1][j] != '#':
              data[i+1][j] += 1

          # 좌
          if j != 0:
            if data[i][j-1] != '#':
              data[i][j-1] += 1

          # 우
          if j != len(data[0])-1: # 가장 끝에 있는지 확인
            if data[i][j+1] != '#':
              data[i][j+1] += 1

          # (왼쪽 대각선) 좌 대각선 상
          if j != 0 and i != 0:
            if data[i-1][j-1] != '#':
              data[i-1][j-1] += 1

          # (왼쪽 대각선) 우 대각선 하
          if j != len(data[0])-1 and i != len(data)-1:
            if data[i+1][j+1] != '#':
              data[i+1][j+1] += 1

          # (왼쪽 대각선) 우 대각선 상
          if j != len(data[0])-1 and i != 0:
            if data[i-1][j+1] != '#':
              data[i-1][j+1] += 1

          # (왼쪽 대각선) 좌 대각선 하
          if j != 0 and i != len(data)-1:
            if data[i+1][j-1] != '#':
              data[i+1][j-1] += 1

  return [sum(data, []).count('#'), sum(list(filter(lambda x:type(x) == int, sum(data, []))))]

print(solution([[0, 0, '#', '#'], ['#', '#', 0, '#'], [0, '#', '#', 0]])) # [7, 16]