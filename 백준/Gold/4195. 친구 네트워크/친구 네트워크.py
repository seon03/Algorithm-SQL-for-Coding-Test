import sys
input = sys.stdin.readline

def find(x):
    if parent[x] == x: return x
    else:
        p = find(parent[x])
        parent[x] = p
        return p

def union(x, y):
    x, y = find(x), find(y)

    if x != y:
        parent[y] = x
        number[x] += number[y]
    print(number[x])

T = int(input())
for _ in range(T):
    F = int(input())
    parent, number = {}, {}
    for i in range(F):
        a, b = input().split()
        if a not in parent:
            parent[a] = a
            number[a] = 1
        if b not in parent:
            parent[b] = b
            number[b] = 1
        union(a, b)