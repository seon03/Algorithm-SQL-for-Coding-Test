n = int(input()) #N의 진짜 약수 개수
d = list(map(int, input().split())) #N의 진짜 약수
print(max(d)*min(d))