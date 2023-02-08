import sys
sys.stdin = open("input.txt", "rt")
from collections import deque
n,k=map(int,input().split())
dp=[0]*100001
q=deque()
q.append(n)
dp[n]=0
while q:
    x=q.popleft()
    if x==k:
        print(dp[k])
        break
    if 0<=x-1<=100000 and not dp[x-1]:
        dp[x-1]=dp[x]+1
        q.append(x-1)
    if 0<=x+1<=100000 and not dp[x+1]:
        dp[x+1]=dp[x]+1
        q.append(x+1)
    if 0<=2*x<=100000 and not dp[2*x]:
        dp[2*x]=dp[x]+1
        q.append(2*x)