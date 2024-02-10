import sys
T = int(sys.stdin.readline())
for _ in range(T):
  N, M = map(int, sys.stdin.readline().split())
  x, y = 1, 1
  for i in range(N):
    x *= M
    M -= 1
    y *= (i+1)
  print(x//y)