import sys
dict = {}
n = int(sys.stdin.readline())
for _ in range(n):
  x, y = sys.stdin.readline().split()
  if y == 'enter':
    dict[x] = True
  else:
    del dict[x]
print('\n'.join(sorted(dict.keys(), reverse=True)))