file = open("demo",'w')
file.write("This is a new line")
file.close()
file = open("demo", 'r')
content = file.read()
print(content)
file = open("demo",'a')
file.write("This is another line which is being appended")
file.close()
file = open("demo",'r')
new = file.read()
print(new)
file.close()



