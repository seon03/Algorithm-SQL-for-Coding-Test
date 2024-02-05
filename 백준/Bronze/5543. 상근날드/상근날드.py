burgers = []
for _ in range(3):
  burgers.append(int(input()))


beverages = []
for _ in range(2):
  beverages.append(int(input()))

set = []
for i in burgers:
  for j in beverages:
    set.append(i + j - 50)

print(min(set))