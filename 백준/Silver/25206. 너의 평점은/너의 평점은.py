rating = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
grade = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]

total, result = 0,0
for _ in range(20):
  x, y, z = input().split()
  y = float(y)
  if z != 'P':
    total += y
    result += y*grade[rating.index(z)]
print(result/total)