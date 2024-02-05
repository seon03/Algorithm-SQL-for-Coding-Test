import sys
N, B = map(int, sys.stdin.readline().split())
list = []
while N != 0:
  if N%B < 10:
    list.append(N%B)
  else:
    list.append(chr(N%B+55))
  N = N//B
list = reversed(list)
for i in list:
  print(i, end="")