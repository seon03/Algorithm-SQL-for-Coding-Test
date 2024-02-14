import sys, math
N = int(sys.stdin.readline())
num = math.factorial(N)
count = 0
for x in str(num)[::-1]:
  if x != '0':
    break
  count += 1
print(count)