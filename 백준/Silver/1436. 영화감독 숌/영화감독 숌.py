import sys
N = int(sys.stdin.readline())
cnt = 0
number = 666

while True:
  if '666' in str(number):
    cnt += 1
  if cnt == N:
    break
  number += 1
print(number)