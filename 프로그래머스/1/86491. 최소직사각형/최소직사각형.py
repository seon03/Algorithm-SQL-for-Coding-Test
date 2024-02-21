def solution(sizes):
    w, h = 0, 0
    for i in sizes:
        if i[0] <= i[1]:
            temp = i[0]
            i[0] = i[1]
            i[1] = temp
    for i in sizes:
        if w < i[0]:
            w = i[0]
        if h < i[1]:
            h = i[1]
    return w*h