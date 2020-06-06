import re
txt = "my name is Mahesh Gadiyar was born in 1987 january 26"
# findall Returns a list containing all matches
x = re.findall("Gadi",txt)
#[]	A set of characters
y= re.findall("[a-m]",txt)
#\	Signals a special sequence (can also be used to escape special characters)
t=  re.findall("\d",txt)
s = re.findall("Ga..r",txt)
print(x)
print(y)
print(t)
print(s)