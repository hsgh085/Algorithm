import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
res = 0
t1_dx = [0, 0, 1, 1]  # 정사각형
t1_dy = [0, 1, 0, 1]
t2_dx = [0, 0, 0]  # 가로길쭉 3칸
t2_dy = [0, 1, 2]
t22_dx = [0, 0, -1, -1, -1, 1, 1, 1]
t22_dy = [-1, 3, 0, 1, 2, 0, 1, 2]
t3_dx = [0, 1, 2]  # 세로길쭉 3칸
t3_dy = [0, 0, 0]
t33_dx = [-1, 0, 0, 1, 1, 2, 2, 3]
t33_dy = [0, -1, 1, -1, 1, -1, 1, 0]
t4_dx = [0, 1, 1]  # ㄴ모양
t4_dy = [0, 0, 1]
t44_dx = [0, 2]
t44_dy = [-1, 1]
t5_dx = [0, 1, 1]  # ㄴ반대모양
t5_dy = [0, -1, 0]
t55_dx = [0, 2]
t55_dy = [1, -1]

for i in range(n):
    for j in range(m):
        sum1, sum2, sum22, sum3, sum33 = 0, 0, 0, 0, 0
        sum4, sum44, sum5, sum55 = 0, 0, 0, 0
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
            for t22 in range(8):
                if 0 <= i+t22_dx[t22] < n and 0 <= j+t22_dy[t22] < m:
                    sum22 = max(sum2+arr[i+t22_dx[t22]][j+t22_dy[t22]], sum22)
        for t3 in range(3):
            if 0 <= i+t3_dx[t3] < n and 0 <= j+t3_dy[t3] < m:
                sum3 += arr[i+t3_dx[t3]][j+t3_dy[t3]]
            else:
                break
        else:
            for t33 in range(8):
                if 0 <= i+t33_dx[t33] < n and 0 <= j+t33_dy[t33] < m:
                    sum33 = max(sum3+arr[i+t33_dx[t33]][j+t33_dy[t33]], sum33)
        for t4 in range(3):
            if 0 <= i+t4_dx[t4] < n and 0 <= j+t4_dy[t4] < m:
                sum4 += arr[i+t4_dx[t4]][j+t4_dy[t4]]
            else:
                break
        else:
            for t44 in range(2):
                if 0 <= i+t44_dx[t44] < n and 0 <= j+t44_dy[t44] < m:
                    sum44 = max(sum4+arr[i+t44_dx[t44]][j+t44_dy[t44]], sum44)
        for t5 in range(3):
            if 0 <= i+t5_dx[t5] < n and 0 <= j+t5_dy[t5] < m:
                sum5 += arr[i+t5_dx[t5]][j+t5_dy[t5]]
            else:
                break
        else:
            for t55 in range(2):
                if 0 <= i+t55_dx[t55] < n and 0 <= j+t55_dy[t55] < m:
                    sum55 = max(sum5+arr[i+t55_dx[t55]][j+t55_dy[t55]], sum55)

        res = max(res, sum1, sum22, sum33, sum44, sum55)
print(res)
