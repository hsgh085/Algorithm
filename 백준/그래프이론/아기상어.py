import sys
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(10**7)
from collections import deque
n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
q=deque()
global sz, eat, time
sz=2
eat=0
time=0
INF=int(217000000)

dx=[1,-1,0,0]
dy=[0,0,-1,1]

#아기 상어 위치 찾기
def findShark():
    for i in range(n):
        for j in range(n):
            if arr[i][j]==9:
                return i,j

#먹을 수 있는 물고기가 있는지 확인하기
def checkFood():
    for i in range(n):
        for j in range(n):
            #먹을 수 있는 물고기가 있는 경우
            if 0<arr[i][j]<sz:
                return 1
    #먹을 수 있는 물고기가 없는 경우
    return 0

# 먹을 수 있는 물고기 중에서 거리가 가까운 물고기가 여러마리라면 그 중에서 가장 우선순위 높은 물고기로 가기 
def findPriorityFood(pos_x, pos_y):
    global sz, time, eat
    q=deque()
    minDis=INF
    arrDis=[[INF]*n for _ in range(n)]
    visited=[[False]*n for _ in range(n)]
    q.append((pos_x, pos_y,0))
    visited[pos_x][pos_y] = True
    res=[]

    while q:
        x,y,d=q.popleft()
        if 0<arr[x][y]<sz:
            arrDis[x][y]=d
            minDis=min(minDis,d)
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if arr[nx][ny]<=sz and visited[nx][ny]==False:
                    visited[nx][ny]=True
                    q.append((nx,ny,d+1))

    if minDis == INF: #아무것도 못 먹은 경우
        print(time)
        exit(0)

    for i in range(n):
        for j in range(n):
            if arrDis[i][j]==minDis:
                res.append((i,j))

    res.sort(key=lambda x:(x[0],x[1])) #우선순위 높은 물고기 위치 구하기
    time+=minDis
    eat+=1
    arr[res[0][0]][res[0][1]]=0
    #아기 상어의 크기 개수만큼 먹었다면 크기 증가
    if eat==sz:
        sz+=1
        eat=0
    findPriorityFood(res[0][0],res[0][1])

pos_x,pos_y=findShark()
arr[pos_x][pos_y] = 0
if checkFood()==0:
    print(0)
else:
    findPriorityFood(pos_x,pos_y)
        