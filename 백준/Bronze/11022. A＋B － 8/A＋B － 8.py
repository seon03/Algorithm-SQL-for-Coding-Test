T = int(input())

for i in range(T):
  A, B = map(int, input().split())
  print("Case #" + str(i+1) + ": " + str(A) + " + " + str(B) + " = " + str(A+B))