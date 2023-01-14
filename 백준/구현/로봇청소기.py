import sys
sys.stdin = open("input.txt", "rt")
n, m = map(int, input().split())
x, y, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dx=[-1,0,1,0] #북, 동, 남, 서
dy=[0,1,0,-1]
cnt = 1
arr[x][y] = 2

while True:
    if arr[x+dx[d-2]][y+dy[d-2]]==2 and arr[x+dx[d]][y+dy[d]]!=0 and arr[x+dx[d-1]][y+dy[d-1]]!=0 and arr[x+dx[d-3]][y+dy[d-3]]!=0:
        x=x+dx[d-2]
        y=y+dy[d-2]
    elif arr[x+dx[d-2]][y+dy[d-2]]==1 and arr[x+dx[d]][y+dy[d]]!=0 and arr[x+dx[d-1]][y+dy[d-1]]!=0 and arr[x+dx[d-3]][y+dy[d-3]]!=0:
        break
    elif arr[x+dx[d-1]][y+dy[d-1]]==0:
        d=(d+3)%4
        arr[x+dx[d]][y+dy[d]]=2
        cnt+=1
        x=x+dx[d]
        y=y+dy[d]
    elif arr[x+dx[d-1]][y+dy[d-1]]!=0:
        d=(d+3)%4
print(cnt)