import sys
from collections import deque
sys.stdin = open("input.txt", "rt")
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
tmp=[[0]*m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def virus(x, y):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if tmp[nx][ny] == 0:
                    tmp[nx][ny] = 2
                    q.append((nx, ny))


def spread():
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 2:
                virus(i, j)


def safe():
    safeCnt = 0
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 0:
                safeCnt += 1
    return safeCnt

res=0
def dfs(cnt):
    global res
    if cnt==3:
        for i in range(n):
            for j in range(m):
                tmp[i][j]=arr[i][j]
        spread()
        res=max(res,safe())
        return

    for i in range(n):
        for j in range(m):
            if arr[i][j]==0:
                arr[i][j]=1
                cnt+=1
                dfs(cnt)
                arr[i][j]=0
                cnt-=1
dfs(0)
print(res)