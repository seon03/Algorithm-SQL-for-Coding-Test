import sys
input = sys.stdin.readline
N = int(input())
A = [0]*N
for i in range(N):
  A[i] = int(input())
A.sort()
for i in range(N):
  A[i] *= (N-i)

A.sort()
print(max(A))