def binarySearch(arr,l,r,x):
    if r<=l:
        return -1
    mid=int((l+r)/2)
    if arr[mid]>x:
        return binarySearch(arr,l,mid,x)
    elif arr[mid]==x:
        return mid
    else:
        return binarySearch(arr,mid,r,x)
    

if __name__=="__main__":
    arr=[1,2,3,4,5,6,7,8,9,10]
    for x in arr:
        index = binarySearch(arr,0,len(arr),x)
        print(index)