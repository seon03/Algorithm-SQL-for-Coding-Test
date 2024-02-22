import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
N, M = map(int, input().split())
cnt = 0

def dfs(idx):
  visited[idx] = True
  for i in range(1, N+1):
    if graph[idx][i] and not visited[i]:
      visited[i] = True
      dfs(i)

graph = [[False] * (N + 1) for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
  u, v = map(int, input().split())
  graph[u][v] = True
  graph[v][u] = True

for i in range(1, N + 1):
  if not visited[i]:
    dfs(i)
    cnt += 1
  
print(cnt)
