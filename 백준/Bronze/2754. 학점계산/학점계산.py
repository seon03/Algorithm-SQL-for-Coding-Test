import sys

input = sys.stdin.readline
score = input()
grade = 0

if score[0] == 'A':
    grade += 4
elif score[0] == 'B':
    grade += 3
elif score[0] == 'C':
    grade += 2
elif score[0] == 'D':
    grade += 1

if score == 'F':
    grade = 0
elif score[1] == '+':
    grade += 0.3
elif score[1] == '-':
    grade -= 0.3

print(float(grade))