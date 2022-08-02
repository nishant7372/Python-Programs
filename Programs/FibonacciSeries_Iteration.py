if __name__=="__main__":
    n = int(input("Enter n:"))
    first = 0
    second = 1
    if n>=0:
        print(first,end=", ")
    if n>=1:
        print(second,end=", ")
    for i in range(2,n+1):
        c=first+second
        print(c,end=", ")
        first,second=second,c
