ABC = [int(input()) for _ in range(3)]
S = str(ABC[0]*ABC[1]*ABC[2])
for i in range(10):
  print(S.count(str(i)))