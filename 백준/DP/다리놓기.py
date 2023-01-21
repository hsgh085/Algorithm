import sys
sys.stdin = open("input.txt", "rt")
input=sys.stdin.readline
num=1
dp=[0]*30
for i in range(1,30):
    num*=i
    dp[i]=num
t=int(input())
for _ in range(t):
    n,m=map(int,input().split()) # mCn
    if n==m:
        print(1)
    else:
        res=dp[m]//(dp[n]*dp[m-n])
        print(res)