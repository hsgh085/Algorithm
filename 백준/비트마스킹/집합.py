import sys
sys.stdin = open("input.txt", "rt")
S=0
m=int(input())
for _ in range(m):
    s=sys.stdin.readline().rstrip()
    if s=="all":
        S=(1<<21)-1
    elif s=="empty":
        S=0
    else:
        command, x=s.split()
        x=int(x)
        if command=="add":
            S|=(1<<x)
        elif command=="remove":
            S&=~(1<<x)
        elif command=="toggle":
            S^=(1<<x)
        elif command=="check":
            if S&(1<<x)==0:
                print(0)
            else:
                print(1)