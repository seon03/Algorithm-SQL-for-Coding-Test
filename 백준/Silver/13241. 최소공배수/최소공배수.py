import sys

input = sys.stdin.readline
def gcd(x, y):
    while y > 0:
        x, y = y, x%y
    return x

def lcm(x, y):
    return x*y // gcd(x, y)

a, b = map(int, input().split())
print(lcm(a, b))