"""# read()

f=open("myfile.txt","r")
data=f.read(10)
print("first part:",data)
f.close()"""

"""#readline()

f=open("myfile.txt","r")
line1=f.readline()
line2=f.readline()
line3=f.readline()
print("line 1:",line1)
print("line 2:",line2)
print("line 3:",line3)
f.close()"""

#readlines()


f=open("myfile.txt","r")
lines=f.readlines()
print("list of lines:",len(lines))
f.close()
