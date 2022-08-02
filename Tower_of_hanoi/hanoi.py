def hanoi(n,source,temp,dest):
    if n==1:
        print("Move disk 1 from {} to {}".format(source,dest))
        return 
    hanoi(n-1,source,dest,temp)
    print("Move disk {} from {} to {}".format(n,source,dest))
    hanoi(n-1,temp,source,dest)


if __name__=="__main__":
    n = int(input("Enter n:"))
    hanoi(n,"A","B","C")