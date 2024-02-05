import sys
T = int(sys.stdin.readline())
def gcd(a, b):
  while b != 0:
    a , b = b, a%b
  return a
for _ in range(T):
  A, B = map(int, sys.stdin.readline().split())
  print(A*B//gcd(A, B))