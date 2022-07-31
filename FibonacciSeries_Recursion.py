def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)

if __name__=="__main__":
    n = int(input("Enter n:"))
    for i in range(0,n+1):
        print(fib(i),end=", ")
