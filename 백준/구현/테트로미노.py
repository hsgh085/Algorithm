import sys
sys.stdin = open("input.txt", "rt")
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
res = 0
t1_dx = [0, 0, 1, 1]  # 정사각형
t1_dy = [0, 1, 0, 1]
t2_dx = [0, 0, 0]  # 가로길쭉
t2_dy = [0, 1, 2]
t3_dx = [0, 1, 2]  # 세로길쭉
t3_dy = [0, 0, 0]
for i in range(n):
    for j in range(m):
        sum1, sum2 = 0, 0
        for t1 in range(4):
            if 0 <= i+t1_dx[t1] < n and 0 <= j+t1_dy[t1] < m:
                sum1 += arr[i+t1_dx[t1]][j+t1_dy[t1]]
            else:
                break
        for t2 in range(3):
            if 0 <= i+t2_dx[t2] < n and 0 <= j+t2_dy[t2] < m:
                sum2 += arr[i+t2_dx[t2]][j+t2_dy[t2]]
            else:
                break
        else:

        res = max(res, sum1, sum2)
print(res)
