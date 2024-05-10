import sys
input = sys.stdin.readline
N, K = map(int, input().split())
A = [0]*N
for i in range(N):
  A[i] = int(input())
A.sort(reverse=True)
num = 0
for coin in A:
  if K >= coin:
    num += K//coin
    K %= coin
  elif K == 0:
    break
  else:
    continue
print(num)