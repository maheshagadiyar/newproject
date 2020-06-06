# set in python
my_set = {1, 2, 3}
print(my_set)
# set can have int, float, string,tuple
my_set2 = {1.0, "hello", (12, 34, 35)}
print(my_set2)
# set cannot have duplicates
# Output: {1, 2, 3, 4}
my_set3 = {1, 2, 3, 4, 3, 2}
print(my_set3)
# we can make set from a list
# Output: {1, 2, 3}
my_set4 = set([1, 2, 3, 2])
print(my_set4)
# Distinguish set and dictionary while creating empty set

# initialize a with {}
a = {}

# check data type of a
print(type(a))

# initialize a with set()
b = set()

# check data type of a
print(type(b))

# Modifying a set in python
my_set5 = {2, 4}
print(my_set5)
# add a string
my_set5.add("mahesh")
print(my_set5)
# add multiple elements
my_set5.update([1, 5])
print(my_set5)
# add set and list
my_set5.update([6, 7], {8, 9, 10})
print(my_set5)
# Difference between discard and remove an element from a set
my_set6 = {1, 2, 3, 4, 5, 6}
print(my_set6)
my_set6.discard(5)
print(my_set6)
my_set6.remove(6)
print(my_set6)
# pop and clear method.
my_set6.pop()
print(my_set6)
my_set6.pop()
print(my_set6)
my_set6.clear()
print(my_set6)
# Python set operations
A ={1,2,3,4,5,6}
B={2,3,7,8,9}
# set union operation
print(A|B)
# or
print(A.union(B))
# set intersection
print(A&B)
#or
print(A.intersection(B))
# set difference
print(A-B)
print(B-A)
#or
print(A.difference(B))
# set symmetic
print(A^B)
#or
print(A.symmetric_difference(B))