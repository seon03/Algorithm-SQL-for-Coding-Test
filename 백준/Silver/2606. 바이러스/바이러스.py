import sys
input = sys.stdin.readline

def dfs(idx):
  global visited, cnt
  visited[idx] = True
  cnt += 1
  for next in range(1, N+1):
    if not visited[next] and graph[idx][next]:
      dfs(next)


N = int(input()) #컴퓨터의 수(노드개수)
M = int(input()) #컴퓨터 쌍의 수(간선개수)
cnt = 0 # 감염되는 컴퓨터의 수

graph = [[False]*(N+1) for _ in range(N+1)]
visited = [False]*(N+1)

#graph 정보 입력
for _ in range(M):
  a, b = map(int, input().split())
  graph[a][b] = True
  graph[b][a] = True

#dfs 수행
dfs(1)
print(cnt-1)