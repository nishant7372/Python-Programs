if __name__=="__main__":
    n = int(input("Enter n:"))
    first = 0
    second = 1
    for i in range(2,n+1):
        c=first+second
        first,second=second,c
    if n<=1:
        print(str(n)+"th term:" , n)
    else: 
        print(str(n)+"th term:", c)
