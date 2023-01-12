import sys
sys.stdin = open("input.txt", "rt")

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()
print(round(sum(arr)/n))  # 산술평균
print(arr[n//2])  # 중앙값
d = dict()
res = []
for x in arr:
    d[x] = 0
for x in arr:
    d[x] += 1
maxFreq = max(d.values())
for key, value in d.items():
    if value == maxFreq:
        res.append(key)
if len(res) == 1:  # 최빈값
    print(res[0])
else:
    print(res[1])
print(arr[-1]-arr[0])  # 범위
