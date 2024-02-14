import sys
N = sys.stdin.readline().strip()
m,x=0,0
for i in range(0,10):
  if i == 6 or i ==9:
    x += N.count(str(i))
  elif m<=N.count(str(i)):
    m = N.count(str(i))
x = x//2 + x%2
print(max(m, x))