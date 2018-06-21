
#ASSIGNMENT 5 DECISION CONTROL STATEMENTS


#1.WAP TO CHECK LEAP YEAR
year=int(input("enter the year"))
if year%4==0:
	print(year,"is a leap year")
else:
		print(year,"is not leap year")

		
		
#2.WAP TO CHECK WHETHER THE DIMENSIONS ARE OF SQUARE OR RECTANGLE

l=int(input("enter the length")) 
b=int(input("enter the breadth"))
if l==b:
	print("the dimensions are of square")
else:
	print("the dimensions are not of square")

	



#3.TAKE THE I/P AGE OF 3 PEOPLE AND DETERMINE OLDEST AND YOUNGEST AMONG THEM
print("please dont enter the same age twice")
P1=int(input("enter age of 1st person"))
P2=int(input("enter age of 2nd person"))
P3=int(input("enter age of 3rd person"))
if P1>P2 and P1>P3:
	print("P1 is oldest")
elif P2>P1 and P2>P3:
	print("P2 is oldest")
else:
	print("P3 is oldest")

	
	
#4.WAP TO CHECK THE PRIZE WON AT DIFFERENT POINTS

x=int(input("enter the points"))
if x>1 and x<=50:
	print("no prize")
elif x>50 and x<=150:
	print("congratulations you have won a wooden dog")
elif x>150 and x<=180:
	print("congratulations you have won a BOOK")
elif x>180 and x<=200:
	print("congratulations you have won a chocklates")
else:
	print("wrong value")

#5.WAP TO CHECK WHETHER USER IS ELIGIBLE for DISCOUNT OR NOT

n=int(input("enter the quantity"))
price=n*100
if price>=1000:
	disc=price*0.1
	print(price-disc)
else:
	print("no discount")