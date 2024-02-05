while True:
  L = input()
  if L == '#':
    break
  else:
    x = 0
    for i in L:
      if i in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
        x += 1
    print(x)