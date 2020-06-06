tuple1 = (2,3,4,4,5,)
print(tuple1)
tuple2 = ("Mahesh","Dinesh","Pooja")
print(tuple2)
print(tuple2 + tuple1)
print(tuple1*3)
print(tuple2[0]+ tuple2[1])
fruits = ("apple","bananan","grapes")
print(fruits[1])
print(tuple1[-2])
print(tuple1[::-1])
y = list(tuple1)
print(y)
y[-1] = "Mahesh"
print(y)
for x in tuple1:
    print(x)
if 2 in tuple1:
    print("yes, '2' is available in tuples")
print(len(tuple1))
r = tuple1.index(5)
print(r)

