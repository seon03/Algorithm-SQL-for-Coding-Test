import sys
n = int(sys.stdin.readline())
list = [0] * (n+1)
list[0] = 0
list[1] = 1
for i in range(2, n+1):
  list[i] = list[i-1] + list[i-2]
print(list[n])