import sys
sys.stdin = open("input.txt", "rt")
input=sys.stdin.readline
n=int(input())
arr=[int(input()) for _ in range(n)]
arr.sort()
if n==1:
    print(arr[0])
    exit(0)
pre_sum=arr[0]+arr[1]
res=pre_sum
for i in range(2,n):
    res+=pre_sum+arr[i]
    pre_sum+=arr[i]
print(res)