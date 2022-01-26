#Question-1

print('Answer-1')

input_string = "Python is a case sensitive language" # Given 

# Part 1.a
print("Ans 1.a--> Length of the input string is:",len(input_string))

# Part 1.b
print("Ans 1.b--> Reverse of input string is:",input_string[::-1]) 

# Part 1.c
sliced_string = input_string[10:26]   
print("Ans 1.c--> Sliced string is:",sliced_string)

# Part 1.d--> Replacing a part of the string
replaced_string=input_string.replace("a case sensitive", "object oriented") 
print("Ans 1.d--> String after replacing is:",replaced_string)

# Part 1.e--> Finding the index of a substring
print("Ans 1.e--> Index of substring \"a\" is:",input_string.index("a")) 

# Part 1.f--> Removing " " from input string
print("Ans 1.f--> String after removing \" \" is:",input_string.replace(" ","") ) 
print()

#************************************************************************************************************************

#Question-2
print('Answer-2')   
name="Tanish Bnasal"
SID=21104079              #initializing
department="EE"
CGPA=9.9
print("Hey, %s Here!"%name)
print("My SID is %d"%SID)
print("I am from %s department and my CGPA is %f"%(department,CGPA))
print()

#************************************************************************************************************************

#Question-3
print('Answer-3')
a=56
b=10

# Part 3.a
print("3.a--> a&b=",a&b)

# Part 3.b
print("3.b--> a|b=",a|b)

# Part 3.c
print("3.c--> a^b=",a^b)

# Part 3.d
print("3.d--> a<<2=",a<<2,"and b<<2=",b<<2)

# Part 3.e
print("3.e--> a>>2=",a>>2,"and b>>4=",b>>4)
print()

#****************************************************************************************************************************

#Question-4
print('Answer-4')                                    
number1=int(input("Enter first number:"))
number2=int(input("Enter second number:"))
number3=int(input("Enter third number:"))

if(number1>number2):
    if(number1>number3):
        greatest_number=number1
    else:
        greatest_number=number3
else:
    if(number2>number3):
        greatest_number=number2
    else:
        greatest_number=number3

print("greatest of three numbers is",greatest_number)
print()

#****************************************************************************************************************************

#Question-5
print('Answer-5')
string=input("Enter a string:")
if "name" in string:
    print("Yes")
else:
    print("No")
print()

#*****************************************************************************************************************************

#Question-6
print('Answer-6')
a=int(input("Enter side a length:"))    #here a,b,c are sides of the triangle
b=int(input("Enter side b length:"))
c=int(input("Enter side c length:"))

# checking condition for triangle.
if a+b>c and a+c>b and b+c>a:
    print("Yes")
else:
    print("No")
    
#**************************************************************************************************************************


#NAME-Tanish bansal
#SID-21104079
#BRACH-EE
