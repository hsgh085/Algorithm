import sys
from collections import deque
sys.stdin = open("input.txt", "rt")
m,n,h=map(int,input().split())
arr=[[[0]*m for _ in range(n)] for _ in range(h)]
for h in range(h):
    arr[h]=[list(map(int,input().split())) for _ in range(n)]
print(arr)