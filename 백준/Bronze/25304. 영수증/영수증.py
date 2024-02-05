X = int(input())

N = int(input())

cost = 0
for _ in range(N):
  a, b = map(int, input().split())
  cost += (a * b)

if cost == X:
  print("Yes")
else:
  print("No")