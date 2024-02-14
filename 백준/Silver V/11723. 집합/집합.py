import sys
S = set()
M = int(sys.stdin.readline())
for _ in range(M):
  do = sys.stdin.readline().strip()
  if do[0:3] == 'add':
    S.add(int(do[4:]))
  elif do[0] == 'r':
    S.discard(int(do[7:]))
  elif do[0] == 'c':
    if int(do[6:]) in S:
      print(1)
    else:
      print(0)
  elif do[0] == 't':
    if int(do[7:]) in S:
      S.remove(int(do[7:]))
    else:
      S.add(int(do[7:]))
  elif do[0:3] == 'all':
    S = set(range(1, 21))
  elif do[0] == 'e':
    S.clear()