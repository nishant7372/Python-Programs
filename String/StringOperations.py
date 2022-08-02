#1. Change a given string to a new string where the first and last chars have been exchanged  --> s[-1:]+s[1:-1]+s[:1]
#2. Reverse a String  --> str[::-1]
#3. Trim String --> str.strip()

def changeString(s):
    s=s[-1:]+s[1:-1]+s[:1]
    return s

def reverseString(s):
    return s[::-1]

def trimString(s):
    return s.strip()

if __name__=="__main__":
   s=input("Enter String:")
   print("New String:",changeString(s))
   print("Reversed String:", reverseString(s))
   print("Trimmed String:", trimString(s))

