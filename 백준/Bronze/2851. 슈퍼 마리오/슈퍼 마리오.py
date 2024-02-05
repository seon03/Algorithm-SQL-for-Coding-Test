score, ans = 0, 0
for _ in range(10):
  score += int(input())
  if 100-ans >= abs(score-100):
    ans = score
print(ans)