import sys
sys.stdin = open("input.txt", "rt")
n=int(input())
arr=[]
lenArr=[]
lenCur=0
for _ in range(n):
    s=input()
    arr.append(s)
    lenArr.append(len(s))
    lenCur=max(lenCur,len(s))
num=9
cmpArr=[]
# def setCmpArr(lenCur):
#     for 