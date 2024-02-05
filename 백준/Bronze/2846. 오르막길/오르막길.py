import sys
N = int(sys.stdin.readline())
P = list(map(int, sys.stdin.readline().split()))
n = 0
list = []
for i in range(1, N):
  if P[i] > P[i-1]:
    n += P[i] - P[i-1]
    list.append(n)
  else:
    n = 0
    list.append(0)
print(max(list))