X, Y = map(int, input().split())
def Rev(X):
  return int(str(X)[::-1])
print(Rev(Rev(X) + Rev(Y)))