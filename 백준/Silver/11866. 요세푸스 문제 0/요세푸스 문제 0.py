import sys
N, K = map(int, sys.stdin.readline().split())
circle = [i+1 for i in range(N)]
yose = []
print('<', end='')
index = K-1
for i in range(N):
  if index <= len(circle)-1:
    yose.append(str(circle.pop(index)))
    index += K-1
  else:
    index = index % len(circle)
    yose.append(str(circle.pop(index)))
    index += K-1
print(', '.join(yose), end='')
print('>', end='')