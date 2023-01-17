import sys
from collections import deque
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    p = list(input().rstrip())
    n = int(input().rstrip())
    s = input().rstrip()
    if n != 0:
        arr = deque(s[1:-1].split(','))
    else:
        arr = deque()

    isR = False
    err = False
    for s in p:
        if s == 'R':
            if isR:
                isR = False
            else:
                isR = True
        else:
            if arr:
                if isR:
                    arr.pop()
                else:
                    arr.popleft()
            else:
                err = True
    if not err:
        if arr:
            if isR:
                arr.reverse()
            l = len(arr)
            print('[', end='')
            for i in range(l-1):
                print(arr[i], end=',')
            print('%s]' % arr[l-1])
        else:
            print('[]')
    else:
        print('error')
