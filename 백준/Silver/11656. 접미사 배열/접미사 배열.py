S = input()
x = [S[i:] for i in range(len(S))]
for i in sorted(x):
    print(i)