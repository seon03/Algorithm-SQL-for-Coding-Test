import sys
input = sys.stdin.readline
N = int(input())
lst = list(map(int, input().split()))

def primenum(x):
    for i in range(2, x):
        if x % i == 0:
            return False

    return True

cnt = 0
for i in lst:
    if i == 1:
        cnt += 0
    elif primenum(i):
        cnt += 1

print(cnt)