import sys
T = int(sys.stdin.readline())
list = [25, 10, 5, 1]
for _ in range(T):
  result = [0]*4
  C = int(sys.stdin.readline())
  for i in range(4):
    if list[i] <= C:
      result[i] = C//list[i]
      C %= list[i]
  print(*result)