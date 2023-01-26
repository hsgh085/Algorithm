import sys
sys.stdin = open("input.txt", "rt")
arr=list(input())
arr.sort(reverse=True)
for x in arr:
    print(x,end='')