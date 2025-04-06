import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
S = input()
PN = 'IO'*N + 'I' #len(PN) = 2N+1
cnt, i, answer = 0, 0, 0
while i < (M-1):
  if S[i:i+3] == 'IOI':
      i += 2
      cnt += 1
      if cnt == N:
        answer += 1
        cnt -= 1
  else:
    i += 1
    cnt = 0  
print(answer)