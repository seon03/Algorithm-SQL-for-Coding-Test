N = input()
temp = N
c = 0
while True:
  if len(N) == 1:
    N = str(int(N)*11)
    c += 1
  else:
    N = str(int(N[1])*10 + (int(N[0]) + int(N[1]))%10)
    c += 1
  if temp == N:
    print(c)
    break