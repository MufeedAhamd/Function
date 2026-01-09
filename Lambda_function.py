''' Lambda Function 
 Lambda function is anonymous function.
 On other word one line fuction'''

# Addding two number
add = lambda a, b : a+b
print("Adding Two Number :",add(2,3))

#  Return multiple result
result = lambda x , y : (x+y,x*y,x-y)
print(result(8,5))

# Upper Case
a = "this is lambda code"
r = lambda a : a.upper()
print(r(a))

# Checking the  number
r = lambda x : "Positive " if x>0 else "Negetive " if x<0 else "Zero"
print(r(-5))
print(r(8))
print(r(0))

# Check for even or odd
r = lambda x: "Even " if x%2 ==0 else "Odd"
print("Given Number is ",r(5))
print("Given Number is ",r(88))


