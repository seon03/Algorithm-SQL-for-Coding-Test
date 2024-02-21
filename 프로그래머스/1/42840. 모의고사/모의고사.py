import math
def solution(answers):
    answer = []
    one = [1,2,3,4,5]*math.ceil(len(answers)/5)
    two = [2,1,2,3,2,4,2,5]*math.ceil(len(answers)/8)
    three = [3,3,1,1,2,2,4,4,5,5]*math.ceil(len(answers)/10)
    x = [one, two, three]
    for i in x:
        cnt = 0
        for j in range(len(answers)):
            if i[j] == answers[j]:
                cnt += 1
        x[x.index(i)] = cnt
    for i in range(3):
        if x[i] == max(x):
            answer.append(i+1)
    return answer