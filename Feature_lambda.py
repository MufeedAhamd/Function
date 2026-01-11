'''
Feature_lambda :
1  Filter
2  Map
3  Reduse
'''

#  Filter is use when we filter a list with peeticuler condition

# #  Extract the even number from list
lst = [12,5,9.3,4,23,45,56,12,32,59]
result = filter(lambda x : x%2==0,lst)
print("Orginal list :",lst)
print("Even list :",list(result))

# # Extract the element that Grater than 20
lst = [12,5,9.3,4,23,45,56,12,32,59]
result = filter(lambda x : x if x> 20 else 0 ,lst)

print("Orginal list :",lst)
print("Udated list :",list(result))


# Map 

# Square every element of list 

lst = [12,5,9.3,4,23,45,56,12,32,59]
result = map(lambda x : x*x , lst)
print("Orginal list :",lst)
print("Square :",list(result))

# Convert string's words into upper case
words = ["python", "data", "science", "ai"]
result = list(map(lambda x: x.upper(), words))
print("Orginal str :",words)
print("update :",list(result))


# Reduce

from functools import reduce # import reduce

# Sum of list
lst = [1,5,2,4,3]
result = reduce(lambda x,y : x+y,lst)
print("List",lst)
print("Sum of list :",result)


# Find the greatest number in list

result = reduce(lambda x ,y:x if x>y else y, lst)
print("List",lst)
print("Graatest number of :",result)