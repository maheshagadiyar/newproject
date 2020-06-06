#A list comprehension generally consist of these parts :
#  Output expression,
#  input sequence,
#  a variable representing member of input sequence and
#  an optional predicate part.
lst = [x**3 for x in range(1,99) if x%2==1]
print(lst)
list2 = [3**x for x in range(100,1000)]
print(list2)
a=12
table= [[a, b, a*b] for b in range (1,20)]
for i in table:
    print(i)
a=13
table= [[a, b, a*b] for b in range (1,20)]
for i in table:
    print(i)
#print[x.lower() for x in ["A","B","C"]]
 lust = [range(1,99)]
 print(lust)