twig = list(map(int, input().split()))
while twig != [1, 2, 3, 4, 5]:
  if twig[0] > twig[1]:
    twig[0], twig[1] = twig[1], twig[0]
    print(*twig)
  if twig[1] > twig[2]:
    twig[1], twig[2] = twig[2], twig[1]
    print(*twig)
  if twig[2] > twig[3]:
    twig[2], twig[3] = twig[3], twig[2]
    print(*twig)
  if twig[3] > twig[4]:
    twig[3], twig[4] = twig[4], twig[3]
    print(*twig)