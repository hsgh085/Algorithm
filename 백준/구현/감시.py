import sys
import copy
sys.stdin = open("input.txt", "rt")

def dfs(graph, depth):
    global answer
    if depth==len(cctv_list):
        answer=min(answer, count_zero(graph))
        return
    else:
        graph_copy=copy.deepcopy(graph)
        x,y,cctv_type=cctv_list[depth]
        for cctv_dir in cctv_direction[cctv_type]:
            watch(x,y,cctv_dir, graph_copy)
            dfs(graph_copy, depth+1)
            graph_copy=copy.deepcopy(graph)

def watch(x,y,direction, graph):
    for d in direction:
        nx,ny=x,y
        while True:
            nx+=direction_list[d][0]
            ny+=direction_list[d][1]
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny]==6:
                    break
                elif graph[nx][ny]==0:
                    graph[nx][ny]='#'
            else:
                break

def count_zero(graph):
    cnt=0
    for i in range(n):
        for j in range(m):
            if graph[i][j]==0:
                cnt+=1
    return cnt
        
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
answer=int(1e9)
cctv_list=[]
for i in range(n):
    for j in range(m):
        if 1<=graph[i][j]<=5:
            cctv_list.append((i,j,graph[i][j]))
direction_list=[(-1,0),(1,0),(0,-1),(0,1)]
cctv_direction=[
    [],
    [[0],[1],[2],[3]],
    [[0,1],[2,3]],
    [[0,2],[0,3],[1,2],[1,3]],
    [[0,1,2],[0,1,3],[0,2,3],[1,2,3]],
    [[0,1,2,3]]
]
dfs(graph, 0)
print(answer)