import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))

dp = P[:]

for i in range(N):
    for j in range(i):
        dp[i] = max(dp[i], P[j] + dp[i-j-1])

print(dp[N-1])