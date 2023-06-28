arr=[3,5,7,9,1]
arr1=[1,2,3,3,3,3,4,4]
arr2=[3,2,4,4,2,5,2,5,5]
arr3=[3,5,7,9,1]

arr.sort()
set_arr=set(arr)
hash={}
for x in set_arr:
    hash[x]=0

for x in arr:
    hash[x]+=1

res=[]
for key, value in hash.items():
    if value!=1:
        res.append(value)
if res:
    print(res)
else:
    print(-1)