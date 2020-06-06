def mulltiply(x):
    return x*2
list1 = [x**(1/2) for x in range (1,20) ]
list2 = [x**2 for x in range (1, 10)]
#print(list)
result = list(map(mulltiply,list1))
result2 = list(map(mulltiply,list2))
print(result,result2)