import sys
input = sys.stdin.readline
T = int(input())
time = [300, 60, 10]
cnt = [0]*3
for i in range(3):
  if time[i] <= T:
    cnt[i] = T // time[i]
    T %= time[i]
  else:
    cnt[i] = 0
if T == 0:
  print(*cnt)
else:
  print(-1)