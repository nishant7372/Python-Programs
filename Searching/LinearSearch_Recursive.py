def linearSearch(arr,x,i):
    if i==len(arr):
        return -1
    if arr[i]==x:
        return i
    return linearSearch(arr,x,i+1)


if __name__=="__main__":
    arr=[1,2,3,4,5,6,7,8,9,10]
    for x in arr:
        index = linearSearch(arr,x,0)
        print(index)