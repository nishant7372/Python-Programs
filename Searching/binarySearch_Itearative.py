
def binarySearch(arr,l,r,x):
    while l<r:
        mid=int((l+r)/2)
        if arr[mid]>x:
            r=mid
        elif arr[mid]==x:
            return mid
        else:
            l=mid
    return -1


if __name__=="__main__":
    arr=[1,2,3,4,5,6,7,8,9,10]
    for x in arr:
        index = binarySearch(arr,0,len(arr),x)
        print(index)