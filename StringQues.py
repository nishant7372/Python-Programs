#Change a given string to a new string where the first and last chars have been exchanged

def changeString(s):
    s=s[-1:]+s[1:-1]+s[:1]
    return s

if __name__=="__main__":
   s=input("Enter String:")
   s=changeString(s)
   print("New String:",s)

