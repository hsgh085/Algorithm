import sys
sys.stdin = open("input.txt", "rt")

s=list(input())
l=len(s)
cnt=0

for i in range(l):
    cnt+=1
    if s[i]=='=':
        if s[i-1]=='c' or s[i-1]=='s':
            cnt-=1
        elif s[i-1]=='z':
            if s[i-2]=='d':
                cnt-=2
            else:
                cnt-=1
    elif s[i]=='-':
        if s[i-1]=='c' or s[i-1]=='d':
            cnt-=1
    elif s[i]=='j':
        if s[i-1]=='l' or s[i-1]=='n':
            cnt-=1
print(cnt)

