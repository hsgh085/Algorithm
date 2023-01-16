import sys
sys.stdin = open("input.txt", "rt")
m = int(input())
s = []
for _ in range(m):
    command = sys.stdin.readline().rstrip()
    if command == "all":
        s = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
             '12', '13', '14', '15', '16', '17', '18', '19', '20']
    elif command == "empty":
        s = []
    else:
        command, x = command.split()
        if command == "add":
            if x not in s:
                s.append(x)
        elif command == "remove":
            l = len(s)
            for i in range(l):
                if s[i] == x:
                    s.pop(i)
                    break
        elif command == "check":
            if x in s:
                print(1)
            else:
                print(0)
        elif command == "toggle":
            l = len(s)
            for i in range(l):
                if s[i] == x:
                    s.pop(i)
                    break
            else:
                s.append(x)
