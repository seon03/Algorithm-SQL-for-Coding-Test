import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
S = input()
PN = 'IO'*N + 'I' #len(PN) = 2N+1
cnt = 0
for i in range(M-2*N):
  if S[i:i+len(PN)] == PN:
    cnt +=1
print(cnt)