D = [0] * 12
D[1:4] = [1, 2, 4]
for i in range(4, 12):
    D[i] = sum(D[i-3:i])

T = int(input())
for _ in range(T):
    N = int(input())
    print(D[N])