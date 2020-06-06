# using map list method
tuplist = [(1,2),(3,4),(5,6),(6,8)]
print("Thr original tuple is :" +str(tuplist))
reslist= list(map(list,tuplist))
print("The updated list it  :" +str(reslist))
# method 2 via using list comprehension
res = [list(i) for i in tuplist]
print("The converted list of list : " + str(res))