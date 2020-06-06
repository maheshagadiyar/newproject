# incase of list slicing provide satarting index, end index value and interval in which you want the list to be printed
list = [x ** 2 for x in range(0, 100) if x ** 2 % 2 == 1]
list2 = [x **3 for x in range(1, 100, 2)]
print(list2)
print(list)
print(list[100::-2])
print(list[:100:10])
print(list[:100:10] * 3)
print(list[25:: -1])
print(list2 [:75:5])
