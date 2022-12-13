import sys
sys.stdin = open("input.txt", "rt")

n = int(input())
rope = []
for _ in range(n):
    rope.append(int(sys.stdin.readline()))
rope.sort()
maxRope = []
for i in range(n):
    maxRope.append(rope[i]*(n-i))
print(max(maxRope))
