import sys
S = int(sys.stdin.readline())
x, count = 0, 0
for i in range(1, S+2):
  x += i
  count = i
  if x > S:
    print(count-1)
    break