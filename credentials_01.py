# 2번. 암호문 (정규표현식)

def credentials(data):
  result = ''
  for i in data:
    result += chr(int(i.replace(" ", "").replace("+", "1").replace("-", "0"), 2))
  return result

print(credentials([' + - - + - + - ', ' + + + - + - + ', ' + + - + + + - '])) # Jun
print(credentials([' + + + - - + + ', ' + + + - + - - ', '++----+', '+++ --+ -', '+++-+ - -'])) # start
print(credentials([' + + - - - - + ', ' + + - + + - - ', '+ +-- +++ ', ' ++- ++++'])) # algo
