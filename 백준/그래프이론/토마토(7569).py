import sys
from collections import deque
sys.stdin = open("input.txt", "rt")
m, n, h = map(int, input().split())
arr = [[[0]*m for _ in range(n)] for _ in range(h)]
for i in range(h):
    for j in range(n):
        arr[i][j] = list(map(int, input().split()))
total = 0
q = deque()
dx = [-1, 1, 0, 0, 0, 0]  # 상,하,좌,우,위,아래
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 0:
                total += 1
            elif arr[i][j][k] == 1:
                q.append((i, j, k))
while q:
    z, x, y = q.popleft()
    for i in range(6):
        nz = z+dz[i]
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m:
            if arr[nz][nx][ny] == 0:
                arr[nz][nx][ny]=arr[z][x][y]+1
                q.append((nz, nx, ny))
res=0
if total==0:
    print(0)
else:
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if arr[i][j][k]==0:
                    print(-1)
                    exit(0)
                res=max(res,arr[i][j][k])
    print(res-1)