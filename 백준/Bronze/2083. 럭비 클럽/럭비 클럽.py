while True:
  x = list(input().split())
  if x[0] == "#" and x[1] == "0" and x[2] == "0":
    break
  else:
    print(x[0] + " Senior" if int(x[1]) > 17 or int(x[2]) >= 80 else x[0] + " Junior")