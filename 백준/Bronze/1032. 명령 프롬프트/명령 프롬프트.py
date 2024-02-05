N = int(input())
x = list(input())
for _ in range(N-1):
  y = list(input())
  for i in range(len(x)):
    if x[i] != y[i]:
      x[i] = "?"
    else:
      continue
print(''.join(x))