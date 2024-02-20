def solution(progresses, speeds):
    import math
    answer = []
    days = []
    count = 1
    for i in range(len(progresses)):
        days.append(math.ceil((100 - progresses[i]) / speeds[i]))
    for i in range(len(days)-1):
        if days[i] >= days[i+1]:
            days[i+1] = days[i]
            count += 1
        else:
            answer.append(count)
            count = 1
    answer.append(count)
    return answer