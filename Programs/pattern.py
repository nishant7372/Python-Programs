'''
Pattern:
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
* 
'''



if __name__=="__main__":
    for i in range(0,5):
        for j in range(0,i+1):
            print("*",end=" ")
        print("")
    for i in range(3,-1,-1):
        for j in range(0,i+1):
            print("*",end=" ")
        print("")
