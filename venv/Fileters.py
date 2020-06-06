listeven= [x**3 for x in range(1,49)]
# print even
even = list(filter(lambda x: x % 2 == 0,listeven))
print(even)
# print odd
odd= list(filter(lambda x: x % 2==1,listeven))
print(odd)
#print square root
root=list(filter(lambda x: x**(1/3),listeven))
print(root)
