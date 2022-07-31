def fib(n):
    if n<2:
        return n
    return fib(n-1)+fib(n-2)

if __name__=="__main__":
    n = int(input("Enter n:"))
    print(str(n)+"th term of Fibonacci Series is:",fib(n))