import sys
N = int(sys.stdin.readline())
data = [[0, 0] for _ in range(N)]
for i in range(N):
  data[i] = list(map(int, sys.stdin.readline().split()))
data.sort()
for i in data:
  print(*i)