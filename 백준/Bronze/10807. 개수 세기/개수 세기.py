N = int(input()) #정수의 개수

I = list(map(int, input().split()))

v = int(input()) #찾으려고 하는 정수

#N개의 정수 중 v는 몇 개인지 출력
result = 0
for i in I:
  if i == v:
    result += 1
  else:
    result += 0
print(result)