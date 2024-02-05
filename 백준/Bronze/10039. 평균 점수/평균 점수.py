sum = 0
for _ in range(5):
  s = int(input())
  if s < 40:
    sum += 40
  else:
    sum += s
    
print(int(sum/5))