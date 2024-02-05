T = int(input())
for _ in range(T):
  N = int(input())
  max = 0
  uni = ""
  for _ in range(N):
    S, L = input().split()
    if max <= int(L):
      max = int(L)
      uni = S
    else:
      continue
  print(uni)