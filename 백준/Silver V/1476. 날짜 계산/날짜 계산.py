import sys
E, S, M = map(int, sys.stdin.readline().split())
e=[15*i+E for i in range(28*19)]
s=[28*i+S for i in range(15*19)]
m=[19*i+M for i in range(15*28)]
for i in e:
  if i in s:
    if i in m:
      print(i)
      break
  else:
    continue