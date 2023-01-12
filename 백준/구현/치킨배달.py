import sys
from itertools import combinations
sys.stdin = open("input.txt", "rt")

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
home = []
chicken = []
tmp = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            home.append((i, j))
        elif arr[i][j] == 2:
            chicken.append((i, j))

res = 217000000
m_chicken = list(combinations(chicken, m))

for mc in m_chicken:
    minDist = 0
    for h in home:
        dist = 217000000
        for c in mc:
            dist = min(abs(h[0]-c[0])+abs(h[1]-c[1]), dist)
        minDist += dist
    res = min(minDist, res)

print(res)
