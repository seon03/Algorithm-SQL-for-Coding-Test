import sys
N = int(sys.stdin.readline())
d = 2
while d <= N:
  if N % d == 0:
    print(d)
    N = N // d
  else:
    d = d + 1