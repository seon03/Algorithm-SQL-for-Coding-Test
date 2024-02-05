S = input()

for i in range(ord('a'), ord('z') + 1):
  print(S.count(chr(i)), end=' ')