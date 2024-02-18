import sys
N = int(sys.stdin.readline())
count = 0
while N > 0:
  if N >= 3:
    N -= 3
    count += 1
  elif N >= 1:
    N -= 1
    count += 1
if count%2 == 1:
  print('SK')
else:
  print('CY')