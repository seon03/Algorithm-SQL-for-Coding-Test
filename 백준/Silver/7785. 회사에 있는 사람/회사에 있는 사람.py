import sys
list = {}
n = int(sys.stdin.readline())
for _ in range(n):
  x, y = sys.stdin.readline().split()
  if y == 'enter':
    list[x] = True
  else:
    del list[x]
print('\n'.join(sorted(list.keys(), reverse=True)))