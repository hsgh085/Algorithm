import sys
sys.stdin = open("input.txt", "rt")
input=sys.stdin.readline
n = int(input())
people = []
res=[]
for _ in range(n):
    x, y = map(int, input().split())
    people.append((x, y))
for i in range(n):
    cnt=0
    for j in range(n):
        if i==j:
            continue
        else:
            if people[i][0]<people[j][0] and people[i][1]<people[j][1]:
                cnt+=1
    res.append(cnt+1)
for x in res:
    print(x, end=' ')