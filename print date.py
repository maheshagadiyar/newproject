from _datetime import datetime
#list = [10, 10, 2019]
#newd = "Date:{0}/{1}/{2}".format(list[0], list[1], list[2])
#print(newd)
today = datetime.today()
d1 = today.strftime("%d/%m/%y")
print(d1)
now = datetime.now()
t2 = now.strftime("%d/%m/%y %H:%M:%S")
print(t2)

