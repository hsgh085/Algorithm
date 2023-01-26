import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline
k, n = map(int, input().split())
arr = [int(input()) for _ in range(k)]
start = 0
end = max(arr)
res = []
while start <= end:
    cnt = 0
    mid = (start+end)//2  # mid=랜선 길이
    if mid==0:
        start=mid+1
        continue
    for x in arr:
        cnt += x//mid
    if cnt < n:
        end = mid-1
    else:
        res.append(mid)
        start = mid+1
print(max(res))