#Prime number smaller than or equal to n using sieve of eratostheses

def sieveOfEratosthenes(n):
    prime = [True for i in range(n+1)]
    p=2
    while(p*p<=n):
        if prime[p]==True:
            for i in range(p*p,n+1,p):
                prime[i]=False
        p+=1
    
    for i in range(2,n+1):
        if prime[i]==True:
            print(i,end=", ")

if __name__ == '__main__':
    n = int(input("Enter n:"))
    print("Prime numbers smaller than or equal to n:", sieveOfEratosthenes(n))    
