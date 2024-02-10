import sys
N = int(sys.stdin.readline())
data = [sys.stdin.readline().strip().split() for _ in range(N)]
data.sort(key = lambda x:int(x[0]))
for i in data:
  print(*i)