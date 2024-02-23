import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dy = [-1, 1, 0, 0, 1, 1, -1, -1]
dx = [0, 0, -1, 1, 1, -1, 1, -1]


def dfs(y, x):
  visited[y][x] = True
  for i in range(8):
    ny = y + dy[i]
    nx = x + dx[i]

    if 0 <= ny < h and 0 <= nx < w:
      if graph[ny][nx] and not visited[ny][nx]:
        dfs(ny, nx)


while True:
  w, h = map(int, input().split())
  if w == 0 and h == 0:
    break

  graph = []
  visited = [[0] * w for _ in range(h)]
  cnt = 0

  for _ in range(h):
    graph.append(list(map(int, input().split())))

  for i in range(h):
    for j in range(w):
      if graph[i][j] and not visited[i][j]:
        dfs(i, j)
        cnt += 1

  print(cnt)
