def solution(brown, yellow):
    answer = []
    y = []
    if yellow == 1:
            y.append([3,3])
    for i in range(2, yellow+1):
        if yellow % i == 0:
            y.append([i+2, yellow//i+2])
    for i in y:
        if i[0]*i[1] == brown+yellow:
            answer.append(max(i[0], i[1]))
            answer.append(min(i[0], i[1]))
            break
    return answer