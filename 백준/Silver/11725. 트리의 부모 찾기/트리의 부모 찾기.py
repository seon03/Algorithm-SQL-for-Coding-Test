import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N = int(input())

def dfs(n):
  global v
  for i in tree[n]:
    if v[i] == False:
      v[i] = n
      dfs(i)

tree = [[] for _ in range(N+1)]
v = [False]*(N+1)

for _ in range(N-1):
  a, b = map(int, input().split())
  tree[a].append(b)
  tree[b].append(a)

dfs(1)
for i in range(2, N+1):
  print(v[i])