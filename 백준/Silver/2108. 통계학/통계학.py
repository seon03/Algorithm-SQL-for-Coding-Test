import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for i in range(N)]

arr.sort()

print(round(sum(arr)/N))  #산술평균
print(arr[N//2])  #중앙값

#최빈값
cnt = Counter(arr)
mode = cnt.most_common()
if len(mode) == 1 or mode[0][1] != mode[1][1]:
  print(mode[0][0])
else:
  print(mode[1][0])

print(max(arr) - min(arr))  #범위