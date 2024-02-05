import sys
while True:
  s = int(sys.stdin.readline())
  if s == 0:
    break
  else:
    if str(s) == str(s)[::-1]:
      print("yes")
    else:
      print("no")