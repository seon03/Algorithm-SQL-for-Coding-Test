for _ in range(3):
  x = list(map(int, input().split()))
  t = (x[3]*3600 + x[4]*60 + x[5]) - (x[0]*3600 + x[1]*60 + x[2])
  print(t//3600, t%3600//60, t%60)