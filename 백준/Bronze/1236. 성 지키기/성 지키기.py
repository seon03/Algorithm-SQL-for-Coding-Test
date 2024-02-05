N, M = map(int, input().split())
list = [input() for _ in range(N)]
n, m = 0, 0
for i in range(N):
  if list[i] == '.'*M:
    n+=1
new = [[""]*N for _ in range(M)]
for i in range(N):
  for j in range(M):
     new[j][i] = list[i][j]
for i in range(M):
  if new[i] == ['.']*N:
    m+=1
print(max(n, m))