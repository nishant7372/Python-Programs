def GCD(a,b):
    if a==0:
        return b
    if b==0:
        return a
    if a==b:
        return a
    if a>b:
        return GCD(a-b,b)
    return GCD(a,b-a)

if __name__=="__main__":
    a=int(input("Enter First Number:"))
    b=int(input("Enter Second Number:"))
    print("GCD of "+str(a)+" and "+str(b)+" is:",GCD(a,b))
