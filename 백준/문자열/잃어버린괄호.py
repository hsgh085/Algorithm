import sys
sys.stdin = open("input.txt", "rt")
s = input().split('-')
plus = list(map(int, s[0].split('+')))
minus = s[1:]
res = sum(plus)
for x in minus:
    m = list(map(int, x.split('+')))
    sum_minus = sum(m)
    res -= sum_minus
print(res)