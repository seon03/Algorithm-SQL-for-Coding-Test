N = int(input())
mem = input()

if mem.count('LL') <= 1:
  print(N)
else:
  print(N - mem.count('LL') + 1)