import sys
sys.stdin = open("input.txt", "rt")

n = int(input())
cnt = 0

for _ in range(n):
    s = list(input())
    isExist = [False]*26
    pred=''
    for x in s:
        idx=ord(x)-97
        if isExist[idx] and pred!=x:
            break
        isExist[idx]=True
        pred=x
    else:
        cnt+=1
print(cnt)