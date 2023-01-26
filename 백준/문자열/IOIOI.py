import sys
from collections import deque
sys.stdin = open("input.txt", "rt")
n = int(input())
m = int(input())
s = list(input())
pn = []
pl=2*n+1
q = deque()
res=0
for i in range(pl):
    if i % 2 == 0:
        pn.append('I')
    else:
        pn.append('O')
for i in range(pl-1):
    q.append(s[i])
for i in range(pl-1,m):
    q.append(s[i])
    for i in range(pl):
        if q[i]!=pn[i]:
            break
    else:
        res+=1
    q.popleft()
print(res)