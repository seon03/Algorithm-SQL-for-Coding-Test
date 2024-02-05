T = int(input())
for _ in range(T):
  m = list(input().split())
  for i in range(len(m)):
    print(str(m[i])[::-1], end=" ")
  print(end="\n")