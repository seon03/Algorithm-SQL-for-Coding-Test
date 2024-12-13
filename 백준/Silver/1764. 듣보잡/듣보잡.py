import sys
input = sys.stdin.readline
N, M = map(int, input().split())
result = []
n = set()
for _ in range(N):
    n.add(input().strip())
m = set()
for _ in range(M):
    m.add(input().strip())
result = sorted(list(n&m))
print(len(result))
for i in result:
    print(i)