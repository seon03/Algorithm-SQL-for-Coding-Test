A, B, C = map(int, input().split()) # 현재시각: 시, 분, 초
D = int(input()) # 요리하는 데 필요한 시간 : 초

E = (A*3600 + B*60 + C + D) % (24*3600)
# 종료되는 시각: 시, 분, 초
F = E // 3600 # 시

G = (E % 3600) // 60 # 분

H = (E % 3600) % 60 # 초

print(F, G, H)