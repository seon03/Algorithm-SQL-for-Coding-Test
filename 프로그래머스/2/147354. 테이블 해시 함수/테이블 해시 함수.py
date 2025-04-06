def solution(data, col, row_begin, row_end):
    result = 0
    data.sort(key=lambda x:[x[col-1], -x[0]])
    
    for i in range(row_begin, row_end+1):
        total = 0
        for j in data[i-1]:
            total += j%i
        result ^= total
    return result