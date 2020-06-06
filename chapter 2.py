food = ["vangibath", "bisibelebath", 'kharabath', 'kesribath', 'tomatobath']
print(food[2])
food.append("mixture")
food.insert(3, "raitha")
# print(food)
#copy method to cpy a list
x = food.copy()
print(x)
# count method to count the value
y = food.count("kharabath")
print(y)
# removes the last element in the list
food.pop()
print(food)
#removes the specified element in the list
food.remove("kesribath")
print(food)
# updates the sorting order of the list
food.sort()
print(food)
# performs list reverse
food.reverse()
print(food)
# multiplay the list element by * operator
food = food*3
print(food)
# add number to the operator
food +=[2]
print(food)
# slicing of the list
#food[:2]
food.pop(0)
print(food)