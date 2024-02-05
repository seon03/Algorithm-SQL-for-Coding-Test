from itertools import combinations_with_replacement
T = int(input())
for _ in range(T):
  num = int(input())
  list = [0] * 45 #삼각수 리스트
  for i in range(45):
    list[i] += list[i-1] + (i+1)
  n = 0
  for i in combinations_with_replacement(list, 3):
    if sum(i) == num:
      n = 1
      break
    else:
      n = 0
  print(n)