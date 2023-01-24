import sys
from collections import deque
sys.stdin = open("input.txt", "rt")
input=sys.stdin.readline
t=int(input())
dx=[-1,-2,-2,-1,1,2,2,1]
dy=[-2,-1,1,2,2,1,-1,-2]
for _ in range(t):
    n=int(input())
    start_x,start_y=map(int,input().split())
    end_x,end_y=map(int,input().split())
    visited=[[False]*n for _ in range(n)]
    q=deque()
    q.append((start_x,start_y,0))
    while q:
        x,y,cnt=q.popleft()
        if x==end_x and y==end_y:
            print(cnt)
            break
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                visited[nx][ny]=True
                q.append((nx,ny,cnt+1))