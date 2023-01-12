num=int(input())
numSet=[0]*10
while num!=0:
    n=num%10
    numSet[n]+=1
    num//=10
if numSet[6]+1<numSet[9] or numSet[6]>numSet[9]+1:
    sum69=numSet[6]+numSet[9]
    if sum69%2==0:
        numSet[6]=sum69//2
        numSet[9]=sum69//2
    else:
        numSet[6]=sum69//2+1
        numSet[9]=sum69//2+1
print(max(numSet))