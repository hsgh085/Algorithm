import sys
from collections import deque
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline
n, m, s = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(n+1):
    graph[i].sort()


def dfs(v, visited):
    if visited[v]:
        return
    else:
        visited[v] = True
        print(v, end=' ')
        for nv in graph[v]:
            dfs(nv, visited)


def bfs():
    q = deque()
    q.append(s)
    visited = [False]*(n+1)
    while q:
        v = q.popleft()
        if not visited[v]:
            visited[v] = True
            print(v, end=' ')
            for nv in graph[v]:
                q.append(nv)


visited = [False]*(n+1)
dfs(s, visited)
print()
bfs()
