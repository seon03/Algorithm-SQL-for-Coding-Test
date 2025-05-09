import sys
input = sys.stdin.readline

A, B = map(int, input().split())
cnt = 1

while B != A:
    if B < A:
        cnt = -1
        break
    if B % 2 == 0:
        B = B // 2
    elif B % 10 == 1:
        B = B // 10
    else:
        cnt = -1
        break
    cnt += 1

print(cnt)