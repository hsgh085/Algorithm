from collections import deque
import sys
sys.stdin = open("input.txt", "rt")

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
home = deque()
chicken = deque()
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            home.append((i, j))
        elif arr[i][j] == 2:
            chicken.append((i, j))
cnt = len(chicken)-m
res = 217000000


def dfs(c):
    global cnt, res
    if c == cnt:
        minDist = 0
        for h in home:
            dist = 217000000
            for c in chicken:
                dist = min(abs(h[0]-c[0])+abs(h[1]-c[1]), dist)
            minDist += dist
        res = min(minDist, res)
        return
    # 위까지는 검증 완료, 아래에서 에러나는 것 같음.
    x, y = chicken.pop()
    c+=1
    dfs(c)
    chicken.append((x, y))
    c -= 1


dfs(0)
print(res)
