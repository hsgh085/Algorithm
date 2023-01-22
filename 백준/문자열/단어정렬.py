import sys
sys.stdin = open("input.txt", "rt")
input=sys.stdin.readline
n=int(input())
arr=[[] for _ in range(51)]
for _ in range(n):
    s=input().rstrip()
    arr[len(s)].append(s)
for i in range(51):
    if arr[i]:
        setArr=list(set(arr[i]))
        setArr.sort()
        for x in setArr:
            print(x)