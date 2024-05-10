import sys
input = sys.stdin.readline
N = int(input())

time = [[0]*2 for _ in range(N)]
for i in range(N):
  start, end = map(int, input().split())
  time[i][0] = start
  time[i][1] = end

time.sort(key = lambda x: (x[1], x[0]))

count = 1
end_time = time[0][1]
for i in range(1, N):
  if time[i][0] >= end_time:
    count += 1
    end_time = time[i][1]
print(count)