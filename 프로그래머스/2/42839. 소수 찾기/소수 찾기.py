from itertools import permutations

def solution(numbers):
    num = [i for i in numbers]
    p = []
    for i in range(1, len(numbers)+1):
        p += list(permutations(num, i))
    for j in p:
        num.append(''.join(j))
    answer = []
    for i in num:
        check = True
        if int(i) < 2:
            continue
        for x in range(2, int(i)):
            if int(i)%x == 0:
                check = False
                break
        if check == True:
            answer.append(int(i))
    return len(set(answer))