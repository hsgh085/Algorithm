import sys
from collections import deque
input=lambda:sys.stdin.readline().rstrip()
sys.stdin = open("input.txt", "rt")
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
max_height = 0
for i in range(n):
    for j in range(n):
        max_height = max(max_height, arr[i][j])

def safe(h):
    cnt = 0
    visited = [[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j] > h and not visited[i][j]:
                q = deque()
                q.append((i, j))
                visited[i][j] = True
                while q:
                    x, y = q.popleft()
                    for d in range(4):
                        nx = x+dx[d]
                        ny = y+dy[d]
                        if 0 <= nx < n and 0 <= ny < n:
                            if arr[nx][ny] > h and not visited[nx][ny]:
                                q.append((nx, ny))
                                visited[nx][ny] = True
                cnt += 1
    return cnt

res=0
for h in range(0,max_height+1):
    res=max(res,safe(h))
print(res)