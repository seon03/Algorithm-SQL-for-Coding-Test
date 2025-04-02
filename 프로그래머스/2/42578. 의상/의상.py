from collections import Counter

def solution(clothes):
    counter = Counter(category for _, category in clothes) # {'headgear': 2, 'eyewear': 1}
    combinations = 1
    for count in counter.values(): # counter.values() = [2, 1]
        combinations *= (count+1)
    return combinations - 1