N = int(input())

# DP 테이블 초기화
D = [0] * 1000001

D[1] = 0
# DP진행
for i in range(2, N+1): #D[1]=0
    D[i] = D[i-1] + 1
    if i % 2 == 0 :
        D[i] = min(D[i], D[i//2] + 1)
    if i % 3 == 0 :
        D[i] = min(D[i], D[i//3] + 1)
 
print(D[N])