def linearSearch(arr,x):
    for i in range(len(arr)):
        if arr[i]==x:
            return i
    return -1


if __name__=="__main__":
    arr=[1,2,3,4,5,6,7,8,9,10]
    for x in arr:
        index = linearSearch(arr,x)
        print(index)