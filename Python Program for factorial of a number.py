# Python 3 program to find
# factorial of given number

#Recursive:

def factorial(n):
    return 1 if( n == 1 or n == 0) else n * factorial(n-1)
#driver code
num = 5
print("Factorial of", num, "is", factorial(num) )

#Iterative:
def factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while(n > 1):
            fact *= n
            n -= 1
        return fact
 
# Driver Code
num = 5;
print("Factorial of",num,"is",
factorial(num))
 

#One line Solution (Using Ternary operator):  
def factorial(n):
     
# single line to find factorial
    return 1 if (n==1 or n==0) else n * factorial(n - 1)
 
 
# Driver Code
num = 5
print ("Factorial of",num,"is", factorial(num))


#By using In-built function:
import math
 
def factoria(n):
    return(math.factorial(n))
 
 
# Driver Code
num = 5
print("Factorial of", num, "is",
      factoria(num))