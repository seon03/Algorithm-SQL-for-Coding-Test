import sys
N = int(sys.stdin.readline())
my_data = [sys.stdin.readline().strip() for _ in range(N)]
my_set = set(my_data)
data = list(my_set)
data.sort()
data.sort(key = len)
for j in data:
  print(j)