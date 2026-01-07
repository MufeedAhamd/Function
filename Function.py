'''
Function are use to store Lines of code that use to repitivily . So that use the function rather than those code.
'''
# For Create a Function Use def Keywords

# Checking Even or Odd

def check(a):    # make Function
    if a%2 ==0:
        return a,"is Even Number"
    else:
        return a,"is Odd Number"
    
a = int(input("Enter a number :"))
# Calling Function
print(check(a))


# Make Calculate the percentage
def Percentage():  
    English= int(input("Enter  English number (Out of Hunderd):"))
    Hindi= int(input("Entert Hindi number (Out of Hunderd):"))
    Math= int(input("Enter  Math number (Out of Hunderd):"))
    Science= int(input("Enter Science number (Out of Hunderd):"))
    SST= int(input("Enter SST number (Out of Hunderd):"))

    Total = English+Hindi+Math+Science+SST
    per = (Total/500)*100

    if per >=90:
        print("You got A+ Grade in your Exam")
    elif per >80 and per<90:
        print("You got A Grade in your Exam")
    elif per >70 and per<80:
        print("You got B Grade in your Exam")
    elif per >60 and per<70:
        print("You got C Grade in your Exam")
    elif per >50 and per<60:
        print("You got D Grade in your Exam")
    else:
        print("your are Fail")

    print("Total Marks (Out of 500) :", Total)
    print(f"Your got {per} %")

Percentage()


# Count Vowels 
def vowel(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count +=1
    return count

s = input("Enter a sentance :")
print(vowel(s))


# Find Duplicate Values
def dup(str):
    str2=[]
    dupli =[]
    for i in str:
        if i in str2:
            dupli.append(i)
        str2.append(i)
    return dupli

str= [] # Make a List
for i in range(10):
    n = int(input("enter the numbers :"))
    str.append(n)

print("Original List :" ,str)
print("Duplicate Values :",dup(str))
            

# Fibonacci Series
def fib(n):
    if n == 1:
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
    

#  Factorial Number
def fact(n):
    if n ==0 or n==1:
        return 1
    else:
        return n* fact(n-1)

n = int(input("Enter the Number :"))
for i in range (1 , n+1):
   x=fact(i)
   print(x , end=' ')