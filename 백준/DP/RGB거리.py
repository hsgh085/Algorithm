import sys
sys.stdin = open("input.txt", "rt")
input=sys.stdin.readline
n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
dpR=[0]*n
dpG=[0]*n
dpB=[0]*n
dpR[0],dpG[0],dpB[0]=arr[0][0],arr[0][1],arr[0][2]
for i in range(1,n):
    dpR[i]=arr[i][0]+min(dpG[i-1],dpB[i-1])
    dpG[i]=arr[i][1]+min(dpR[i-1],dpB[i-1])
    dpB[i]=arr[i][2]+min(dpG[i-1],dpR[i-1])
print(min(dpR[n-1],dpG[n-1],dpB[n-1]))