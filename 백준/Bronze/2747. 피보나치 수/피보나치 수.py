import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * (N+1) 

if N == 1:
  dp[1] = 1
  print(dp[1])
elif N == 2:
  dp[2] = 1
  print(dp[2])
else:
  dp[1] = 1
  dp[2] = 1
  for i in range(3, N+1):
    dp[i] = dp[i-1] + dp[i-2]
  print(dp[N])