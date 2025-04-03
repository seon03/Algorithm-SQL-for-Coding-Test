import sys
input = sys.stdin.readline
n, m = map(int, input().split())
S = [input() for _ in range(n)]
count = 0
for _ in range(m):
  spec = input()
  if spec in S:
    count += 1
print(count)