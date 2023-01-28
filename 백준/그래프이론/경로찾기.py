import sys
from collections import deque
sys.stdin = open("input.txt", "rt")
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
graph = [[] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            graph[i].append(j)
res = [[0]*n for _ in range(n)]


def bfs(v, res):
    q = deque()
    q.append(v)
    visited = [False]*n
    while q:
        x = q.popleft()
        for nx in graph[x]:
            if not visited[nx]:
                visited[nx] = True
                q.append(nx)
    for j in range(n):
        if visited[j]:
            res[v][j] = 1


for i in range(n):
    bfs(i, res)
for i in range(n):
    for j in range(n):
        print(res[i][j], end=' ')
    print()
