T = int(input())
for _ in range(T):
  S = input()
  add = 0
  count = 0
  for i in range(len(S)):
    if S[i] == 'O':
      add += 1
    else:
      add = 0
    count += add
  print(count)