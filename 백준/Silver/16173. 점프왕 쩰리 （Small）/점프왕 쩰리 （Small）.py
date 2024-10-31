from collections import deque

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

dx = [1, 0]
dy = [0, 1]


def bfs(x, y):
    q = deque()
    q.append([x, y])

    while q:
        x, y = q.popleft()
        step = graph[x][y]

        if graph[x][y] == -1:
              return True
        for move in range(2):
            nx = x + dx[move]*step
            ny = y + dy[move]*step

            if nx < 0 or nx >= N or ny <0 or ny >= N:
                continue
  
            if not visited[nx][ny]:
                visited[nx][ny] = True
                q.append([nx, ny])


if bfs(0, 0):
    print('HaruHaru')
else:
    print('Hing')
