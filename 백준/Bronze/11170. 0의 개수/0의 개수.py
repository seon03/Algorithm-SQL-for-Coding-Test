import sys
T = int(sys.stdin.readline())
for _ in range(T):
  N, M = map(int, input().split())
  x = 0
  for i in range(N, M+1):
    x += str(i).count("0")
  print(x)