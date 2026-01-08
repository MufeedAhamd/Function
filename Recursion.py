'''Practice Recursion Function 
'''

# Factorial of a Number
def fact(n):
    if n ==0 or n == 1:
       return 1
    else:
        return  n* fact(n-1)
 
n = int(input("Enter a number :"))
print(f"Factorial of {n} is : {fact(n)}")


# Fibonacci Sequence
def fib(n):
    if n==1 :
        return 0
    elif n==2:
        return 1
    else:
        result = fib(n-1)+fib(n-2)
        return result
    
n = int(input("Enter the Number :"))
for i in range (1 , n+1):
   x=fib(i)
   print(x , end=' ')


# Power Calculation
def power(a,b):
    if a == 0 :
        return 0
    elif b==0:
        return 1
    else:
        result = a*power(a,b-1)
        return result
    
n = int(input("Enter a number :"))
p = int(input("Enter the power :"))
print(f"{n} power of {p} is :",power(n,p))



# Length of a String
def lenght(str):
    if str == "":
        return 0
    else:
        return 1 +lenght(str[1:])
    
str = input("Enter a string :")
print(f"The lenght of this string {str} : {lenght(str)}")


# Sum of Array Elements
def add(lst):
    if len(lst) ==0:
        return 0
    else:
        return lst[0]+ add(lst[1:])

lst =[2,3,5]
print("Sum of list :",add(lst))
