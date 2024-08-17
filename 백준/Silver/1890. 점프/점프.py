import sys
input = sys.stdin.readline

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*N for _ in range(N)]
dp[0][0] = 1

for i in range(N):
  for j in range(N):
    if dp[i][j] > 0 and arr[i][j] > 0:
      jump = arr[i][j]
      if j + jump < N:
        dp[i][j+jump] += dp[i][j]
      if i + jump < N:
        dp[i+jump][j] += dp[i][j]
print(dp[N-1][N-1])