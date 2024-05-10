import sys
input = sys.stdin.readline
N = int(input())
Pi = map(int, input().split())
sum = 0
min = 0
for i in sorted(Pi):
  sum += i
  min += sum
print(min)