import sys
sys.stdin = open("input.txt", "rt")
from collections import deque
input=sys.stdin.readline
n=int(input())
arr=[[0]*(n+2) for _ in range(n+2)]
arr[1][1]=1 #1:뱀, 2:벽, 3:사과
# 벽 생성
for i in range(n+2):
    arr[0][i]=2
    arr[n+1][i]=2
    arr[i][0]=2
    arr[i][n+1]=2
# 사과 위치
k=int(input())
for _ in range(k):
    x,y=map(int,sys.stdin.readline().rstrip().split())
    arr[x][y]=3
l=int(input())
dir=deque()
for _ in range(l):
    t,d=sys.stdin.readline().rstrip().split()
    t=int(t)
    dir.append((t,d)) 
dx=[-1,0,1,0] #북,동,남,서
dy=[0,1,0,-1]
d_idx=1
snakeLen=1
time=0
x,y=1,1 #뱀 머리 위치
xe,ye=1,1
snake=deque() #뱀의 모든 위치
snake.append((1,1))
t,d=dir.popleft()
while True:
    # for i in range(n+2):
    #     print(arr[i])
    # print(snake)
    # print("뱀머리:",x,y)
    # print("뱀꼬리:",xe,ye)
    # print(time,"초 후")
    # print()
    if time==t:
        if d=="L":
            d_idx=(d_idx-1)%4
        elif d=="D":
            d_idx=(d_idx+1)%4
        if dir:
            t,d=dir.popleft()
    nx=x+dx[d_idx]
    ny=y+dy[d_idx]
    time+=1
    if arr[nx][ny]==1 or arr[nx][ny]==2:
        print(time)
        break
    snake.append((nx,ny))
    if arr[nx][ny]==0:
        xe,ye=snake.popleft() #뱀 꼬리
        arr[xe][ye]=0
    elif arr[nx][ny]==3:
        snakeLen+=1
    arr[nx][ny]=1
    x,y=nx,ny