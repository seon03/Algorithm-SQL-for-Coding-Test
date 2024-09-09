import sys
input = sys.stdin.readline
N = int(input())
lst = [0]
for _ in range(N):
    lst.append(int(input()))
dp = [0]*(N+1)
dp[1] = lst[1]
if N > 1:
    dp[2] = lst[1] + lst[2]
    for i in range(3, N+1):
        dp[i] = max(dp[i-3]+lst[i-1]+lst[i], dp[i-2]+lst[i], dp[i-1])
print(max(dp))