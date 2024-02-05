import sys
N = int(sys.stdin.readline())
for _ in range(N):
  a = sys.stdin.readline().split()
  b = sys.stdin.readline().split()
  if a[1:].count("4") > b[1:].count("4"):
    print("A")
  elif a[1:].count("4") < b[1:].count("4"):
    print("B")
  else:
    if a[1:].count("3") > b[1:].count("3"):
      print("A")
    elif a[1:].count("3") < b[1:].count("3"):
      print("B")
    else:
      if a[1:].count("2") > b[1:].count("2"):
        print("A")
      elif a[1:].count("2") < b[1:].count("2"):
        print("B")
      else:
        if a[1:].count("1") > b[1:].count("1"):
          print("A")
        elif a[1:].count("1") < b[1:].count("1"):
          print("B")
        else:
          print("D")