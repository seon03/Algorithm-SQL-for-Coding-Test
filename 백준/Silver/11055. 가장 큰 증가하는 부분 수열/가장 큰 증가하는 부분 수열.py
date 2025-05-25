import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
dp = [0]*n
dp[0] = a[0]

for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[j]+a[i], dp[i])
        else:
            dp[i] = max(dp[i], a[i])

print(max(dp))