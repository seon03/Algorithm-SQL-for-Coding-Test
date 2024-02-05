n = list(map(int, input().split()))

p = ( n[0]**2 + n[1]**2 + n[2]**2 + n[3]**2 + n[4]**2 ) % 10

print(p)