import sys
input = sys.stdin.readline
N = int(input())
num = list(map(int, input().split()))
M = int(input())
arr = list(map(int, input().split()))
dict = {}
for i in num:
  if i in dict:
    dict[i] += 1
  else:
    dict[i] = 1
for i in arr:
  if i in dict:
    print(dict[i], end = ' ')
  else:
    print(0, end = ' ')