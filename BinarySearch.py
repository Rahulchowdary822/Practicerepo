array = []
n=int(input("Enter the number of elements: "))
for i in range(n):
    array.append(int(input()))
searchKey = int(input("Enter the element to search: "))
low=0
high=len(array)-1
while low <= high:
    mid = low + (high - low)//2
    if array[mid] == searchKey:
        print("Element found at index: ",mid)
        break
    elif array[mid] < searchKey:
        low = mid + 1
    else:
        high = mid - 1