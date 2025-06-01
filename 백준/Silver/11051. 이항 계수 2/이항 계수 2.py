import sys
input = sys.stdin.readline

N, K = map(int, input().split())
a, b = 1, 1
for i in range(K):
    a *= N
    N -= 1

for i in range(1, K+1):
    b *= i

print((a//b)%10007)