
def calculator(choice,a,b):
    if choice=="1":
        return a+b
    elif choice=="2":
        return a-b
    elif choice=='3':
        return a*b
    elif choice=="4":
        return a/b
    else: 
        return "Invalid Choice"

if __name__=="__main__":
    first = float(input("Enter first Number:"))
    second = float(input("Enter Second Number:"))
    print("press -");
    print("1 - Addition")
    print("2 - Subtraction")
    print("3 - Multiplication")
    print("4 - Division")
    choice = input("Enter your Choice")
    res = calculator(choice,first,second)
    print(res)

     