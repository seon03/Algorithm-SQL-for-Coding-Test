a = [k for k in range(1, 10001)]
b = []
for i in range(1, 10001):
  for j in str(i):
    i += int(j)
  b.append(i)
a = sorted(set(a) - set(b))
for i in a:
  print(i)