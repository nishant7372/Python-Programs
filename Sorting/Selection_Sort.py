def swap(i,j,list):
    list[i],list[j]=list[j],list[i]

def selectionSort(list):
    for j in range(len(list)):
        min=j
        for i in range(j+1,len(list)):
            if list[i]<list[min]:
                min=i
        swap(j,min,list)


if __name__=="__main__":
    list=[2,7,5,4,3,6]
    selectionSort(list)
    print("Sorted List:",list)
