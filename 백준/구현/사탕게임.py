import sys
sys.stdin = open("input.txt", "rt")
input=sys.stdin.readline
n=int(input())
arr=[list(input()) for _ in range(n)]

def findMax(x,y):
    res=0
    predC,predR=arr[x][0],arr[0][y]
    cntC,cntR=1,1
    for i in range(1,n):
        if arr[x][i]==predC:
            cntC+=1
        else:
            res=max(res,cntC)
            predC=arr[x][i]
            cntC=1
        if arr[i][y]==predR:
            cntR+=1
        else:
            res=max(res,cntR)
            predR=arr[i][y]
            cntR=1
    res=max(res,cntC,cntR)
    return res

maxCandy=0
for i in range(n):
    maxCandy=max(maxCandy,findMax(i,i))

for i in range(n):
    for j in range(0,n-1):
        if arr[i][j]!=arr[i][j+1]:
            arr[i][j],arr[i][j+1]=arr[i][j+1],arr[i][j]
            maxCandy=max(maxCandy,findMax(i,j),findMax(i,j+1))
            arr[i][j],arr[i][j+1]=arr[i][j+1],arr[i][j]
        if arr[j][i]!=arr[j+1][i]:
            arr[j][i],arr[j+1][i]=arr[j+1][i],arr[j][i]
            maxCandy=max(maxCandy,findMax(j,i),findMax(j+1,i))
            arr[j][i],arr[j+1][i]=arr[j+1][i],arr[j][i]
print(maxCandy)