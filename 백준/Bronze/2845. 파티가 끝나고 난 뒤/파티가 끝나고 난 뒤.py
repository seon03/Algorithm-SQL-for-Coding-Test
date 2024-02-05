L, P = map(int, input().split())

news = list(map(int, input().split()))

for i in range(5):
  print(news[i] - L*P, end=' ')