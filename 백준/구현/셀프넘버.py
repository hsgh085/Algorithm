n = 1
isSelfNum = [True]*10001

while n < 10001:
    new_n = n
    d_n = n
    while new_n != 0:
        d_n += new_n % 10
        new_n //= 10
    if d_n<10001:
        isSelfNum[d_n] = False

    if isSelfNum[n]:
        print(n)
    n += 1