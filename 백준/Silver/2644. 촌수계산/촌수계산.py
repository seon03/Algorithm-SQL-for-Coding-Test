import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
a, b = map(int, input().split())
m = int(input())

def dfs(v, num):
  num += 1
  visited[v] = True

  if v == b:
    result.append(num)

  for i in range(n+1):
    if graph[v][i] and not visited[i]:
      dfs(i, num)
     

graph = [[False]*(n+1) for _ in range(n+1)]
visited = [0]*(n+1)
result = []

for _ in range(m):
  x, y = map(int, input().split())
  graph[x][y] = True
  graph[y][x] = True

dfs(a, 0)
if len(result) == 0:
  print(-1)
else:
  print(result[0]-1)