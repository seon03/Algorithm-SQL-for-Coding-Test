N, K = map(int, input().split())
n = 1
k = 1
for i in range(1, K+1):
  n *= (N-i+1)
  k *= i
print(n//k)