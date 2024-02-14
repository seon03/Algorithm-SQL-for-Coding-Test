import bisect, sys
N = int(sys.stdin.readline())
n = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
m = list(map(int, sys.stdin.readline().split()))
n.sort()
for i in m:
  l=bisect.bisect_left(n, i)
  r=bisect.bisect_right(n, i)
  print(r-l, end=' ')