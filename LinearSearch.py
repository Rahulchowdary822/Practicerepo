Nums=list(map(int,input().split()))
searchKey=int(input())
flag=0
indx=0
for i in range(len(Nums)):
    if Nums[i]==searchKey:
        flag=1
        indx=i
if flag==1:
    print("Key Found at Index: ",indx)