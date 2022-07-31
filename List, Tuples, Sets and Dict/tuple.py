#tuples are immutable, so you can not add new elements

def addItemUsingConcat(item,tpl):
    tpl=tpl+(item,) #concatenation of tuple, it will create a new tuple
    return tpl

def accessingTuple(tpl):
    for i in range(len(tpl)):
        print(tpl[i],end=", ")  #accessing tuple items using index

def addItemUsingConversion(item,tpl):
    list1 = list(tpl)  #conversion of tuple to list
    list1.append(item) #adding new item to list
    tpl = tuple(list1) #converting list to tuple
    return tpl

def slicing(tpl):
    print(tpl[2:5])          #from index 2 to 4
    print(tpl[0:])           #from index 0 to len(tpl)-1
    print(tpl[:len(tpl)])    #from index 0 to len(tpl)-1
    print(tpl[:-1])          #from index 0 to len(tpl)-2
    print(tpl[::2])          #all even indices

if __name__=="__main__":
    tpl=("Apple","Banana","Cherry","Guava","PineApple")
    print(type(tpl))
    print(tpl)

    tpl=addItemUsingConcat("Mango",tpl)
    print(tpl)

    accessingTuple(tpl)

    tpl=addItemUsingConversion("Berry",tpl)
    print("\n",tpl)

    slicing(tpl)


    