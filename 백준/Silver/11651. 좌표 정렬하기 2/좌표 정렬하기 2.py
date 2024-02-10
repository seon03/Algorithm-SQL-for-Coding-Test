import sys
N = int(sys.stdin.readline())
data = []
for _ in range(N):
  data.append(list(map(int, sys.stdin.readline().split())))
data.sort(key = lambda x:(x[1],x[0]))
for i in data:
  print(*i)