from itertools import combinations
from math import lcm
N = list(map(int, input().split()))
list = []
for i in combinations(N, 3):
 list.append(lcm(*i))
print(min(list))