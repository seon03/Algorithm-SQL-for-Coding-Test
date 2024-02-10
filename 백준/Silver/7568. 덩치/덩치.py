import sys
N = int(sys.stdin.readline())
data = []
for _ in range(N):
  data.append(list(map(int, sys.stdin.readline().split())))
for i in range(N):
  rank = 1
  for j in range(N):
    if i != j:
      if (data[i][0] < data[j][0]) and (data[i][1] < data[j][1]):
        rank += 1
  print(rank, end=' ')