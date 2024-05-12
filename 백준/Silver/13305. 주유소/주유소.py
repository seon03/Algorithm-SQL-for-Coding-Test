import sys
input = sys.stdin.readline
N = int(input())
road = list(map(int, input().split()))
cost = list(map(int, input().split()))
min = cost[0]*road[0]
for i in range(1, len(road)):
  if cost[i] > cost[i-1]:
    cost[i] = cost[i-1]
  
  min += cost[i]*road[i]
print(min)