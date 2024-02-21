import sys
input = sys.stdin.readline

def dfs(idx):
    global visited
    visited[idx] = True
    print(idx, end=' ')
    for next in range(1, N+1):
        if not visited[next] and graph[idx][next]:
            dfs(next)#재귀

def bfs():
    global q, visited
    while q: #q가 비어 있기 전까지 반복
        cur = q.pop(0)
        print(cur, end=' ')
        for next in range(1, N+1):
            if not visited[next] and graph[cur][next]:
                visited[next] = True
                q.append(next)
            
N, M, V = map(int, input().split())
graph = [[False]*(N+1) for _ in range(N+1)]
visited = [False]*(N+1)
#graph
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True
#dfs
dfs(V)
print()

#bfs
visited = [False]*(N+1)
q = [V]
visited[V] = True
bfs()