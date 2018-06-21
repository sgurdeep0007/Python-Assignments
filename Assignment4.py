#DICTIONARIES

#1.CREATE A DICTIONARY TO STORE NAME AND MARKS OF 10 STUDENTS BY USER I/P

d={}
name=input("enter the name")
marks=input("enter the marks")
d[name]=marks
name=input("enter the name")
marks=input("enter the marks")
d[name]=marks
name=input("enter the name")
marks=input("enter the marks")
d[name]=marks
name=input("enter the name")
marks=input("enter the marks")
d[name]=marks
name=input("enter the name")
marks=input("enter the marks")
d[name]=marks
name=input("enter the name")
marks=input("enter the marks")
d[name]=marks
name=input("enter the name")
marks=input("enter the marks")
d[name]=marks
name=input("enter the name")
marks=input("enter the marks")
d[name]=marks
name=input("enter the name")
marks=input("enter the marks")
d[name]=marks
name=input("enter the name")
marks=input("enter the marks")
d[name]=marks
print(d)

#2.Sort the dictionary created in previous question A.T marks

d={}
name=input("enter the name")
marks=input("enter the marks")
d[name]=marks
name=input("enter the name")
marks=input("enter the marks")
d[name]=marks
name=input("enter the name")
marks=input("enter the marks")
d[name]=marks
name=input("enter the name")
marks=input("enter the marks")
d[name]=marks
name=input("enter the name")
marks=input("enter the marks")
d[name]=marks
name=input("enter the name")
marks=input("enter the marks")
d[name]=marks
name=input("enter the name")
marks=input("enter the marks")
d[name]=marks
name=input("enter the name")
marks=input("enter the marks")
d[name]=marks
name=input("enter the name")
marks=input("enter the marks")
d[name]=marks
name=input("enter the name")
marks=input("enter the marks")
d[name]=marks
print(d)
l=list(d.values())
l.sort()
print(l)


#3.COUNT THE REPEATED LETTER IN WORD "MISSISSIPPI"
l=list("MISSISSIPPI")
print(l.count('M'))
print(l.count('I'))
print(l.count('S'))
print(l.count('P'))


#TUPPLES


#1.WAP TO CREATE A TUPPLE WITH DIFFERENT DATA TYPES
t=(2,3.5,7,7.0,'g')
len(t)
print(t)
print(len(t))


#2.FIND MAX AND MIN IN A TUPPLE
t=(2,3.5,7,7.0,20.0,20,2.0)
print(max(t))
print(min(t))


#3.WAP TO FIND THE PRODUCT OF ALL ELEMENTS OF A TUPPLE
t=(2,3,8,10)
product=t[0]*t[1]*t[2]*t[3]
print("product=",product)




#SETS


#1.CREATE TWO SETS USING USER DEFINED VALUES
x1=input("enter the value")
y1=input("enter the value")
z1=input("enter the value")

x2=input("enter the value")
y2=input("enter the value")
z2=input("enter the value")

S1=(set([x1,y1,z1]))
S2=(set([x2,y2,z2]))
#1.1
print(S1-S2)
#1.2
print(S1==S2)
#1.3
print(S1 & S2)




