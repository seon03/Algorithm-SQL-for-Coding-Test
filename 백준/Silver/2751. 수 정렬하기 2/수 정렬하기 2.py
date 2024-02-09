import sys
N = int(sys.stdin.readline())
list = [int(sys.stdin.readline().strip()) for _ in range(N)]
list.sort()
for i in list:
  print(i)