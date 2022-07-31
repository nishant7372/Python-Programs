from itertools import count


def addItem(item,fruits):
    fruits.append(item)  #append at last

def addItemUsingIndex(item,index,fruits):
    fruits.insert(index,item)   #add at particular index

def deleteItem(item,fruits):
    fruits.remove(item)   #delete using item value

def deleteItemUsingIndex(index,fruits):
    fruits.pop(index)   #delete from particular index  (if no index--> delete last item)

def countItem(item,fruits):
    return fruits.count(item)

def check(item,fruits):
    if item in fruits:
        print(item +" is present in fruits")
    else:
        print(item +" is not present in fruits")

if __name__=="__main__":
    fruits = ["Apple","Banana","Cherry","Guava"]
    print(type(fruits))
    print(fruits)
    addItem("Mango",fruits)
    print(fruits)
    addItemUsingIndex("Mango",2,fruits)
    print(fruits)
    count=countItem("Mango",fruits)
    print(count)
    deleteItem("Mango",fruits)
    print(fruits)
    deleteItemUsingIndex(1,fruits)
    print(fruits)
    check("Mango",fruits)
    deleteItem("Mango",fruits)
    print(fruits)
    check("Mango",fruits)
    vegetables=["Kadoo","Baigan","Bhindi"]
    fruits.extend(vegetables)
    print(fruits)
    vegetables=("Kadoo","Baigan","Bhindi")
    fruits.extend(vegetables)
    print(fruits)
    vegetables={"Kadoo","Baigan","Bhindi"}
    fruits.extend(vegetables)
    print(fruits)
    print(fruits.index("Baigan")) #list.index method