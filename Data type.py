#Data type string
x = "This is a string "
print(x)
#Data type is int
y= int(20)
z=int(22.5)
print(y)
print(z)
#Data type is FLoat
a = float(3.5)
print(a)
#Data type is complex
b=1j
print(b)
#Data type is list
mylist =["Apple","Banana","Grapes"]
print(mylist)
# data type tuple
mytuple = ("Mango","chikoo","Kiwi")
print(mytuple)
# range
y = range(15)
print(y)
# frozen set
num =(1, 2,3,4,5,6,4,3,2)
enum= frozenset(num)
print(enum)
#frozenset
Student = {"name": "Ankit", "age": 21, "sex": "Male",
           "college": "MNNIT Allahabad", "address": "Allahabad"}
key=(frozenset(Student))
print(key)
#bytarray
t= bytearray(6)
print(t)
print(type(t))
#memoryview
s= memoryview(bytes(5))
print(s)
print(type(s))
