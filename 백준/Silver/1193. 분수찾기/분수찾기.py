import sys
X = int(sys.stdin.readline())
n = 1
while X - n*(n+1)//2 > 0:
  n += 1
key = X - (n-1)*n//2
if n%2 == 0:
  print(str(key) + '/' + str(n+1-key))
else:
  print(str(n+1-key) + '/' + str(key))