import sys
sys.stdin = open("input.txt", "rt")
from collections import deque
m,n=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]
q=deque()
cnt0=0
dx=[0,0,1,-1]
dy=[1,-1,0,0]

for i in range(n):
    for j in range(m):
        if arr[i][j]==1:
            q.append((i,j))
        elif arr[i][j]==0:
            cnt0+=1

if cnt0==0:
    print(0)
else:
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if arr[nx][ny]==0:
                    arr[nx][ny]=arr[x][y]+1
                    cnt0-=1
                    q.append((nx,ny))
    if cnt0!=0:
        print(-1)
    else:
        res=0
        for i in range(n):
            maxI=max(arr[i])
            res=max(res,maxI)
        print(res-1)