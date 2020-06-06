list = [x for x in range(3, 11)]
print(list)
list3_6 = list[3:6]
print(list3_6)
##  below list has numbers from 2 to 5
list2_5 = list[1:5]
print(list2_5)
##  below list has numbers from 6 to 8
list5_8 = list[5:8]
print(list5_8)
#  below list has numbers from 2 to 10
list2_10 = list[1:]
print(list2_10)
#  below list has numbers from 1 to 5
list1_5 = list[:5]
print(list1_5)
#  below list has numbers from 10 to 1
rev_list = list[:: -1]
print(rev_list)


def rev(longlist):
    newlst = list[:: -1]
    return newlst


longlist = [x ** 3 for x in range(1, 99)]

print(rev(longlist))
