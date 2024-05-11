import sys
input = sys.stdin.readline

m = 1000 - int(input())

coin = [500, 100, 50, 10, 5, 1]

cnt = 0
for i in coin:
  if m >= i:
    cnt += m // i
    m %= i
print(cnt)